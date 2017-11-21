import csv
import models
import configs
import datetime
import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shapely.geometry import Point
from shapely.wkt import dumps
from io import StringIO


def int_or_none(val):
    return int(val) if val is not "" else None


def float_or_none(val):
    return float(val) if val is not "" else None


def format_row(row):

    # Format location field into WKT
    try:
        location = dumps(Point(float(row['LONGITUDE']), float(row['LATITUDE'])))
    except (AttributeError, ValueError):
        location = None

    # Create date object, none if missing  fields

    try:
        earthquake_date = datetime.date(
            int_or_none(row["YEAR"]),
            int_or_none(row["MONTH"]),
            int_or_none(row["DAY"])
        ).isoformat()

    except Exception:
        earthquake_date = None

    return {
        'id': row["I_D"],
        'name': row["LOCATION_NAME"],
        'date': earthquake_date,
        'location': location,
        'hour': int_or_none(row["HOUR"]),
        'year': int_or_none(row["YEAR"]),
        'month': int_or_none(row["MONTH"]),
        'day': int_or_none(row["DAY"]),
        'minute': int_or_none(row["MINUTE"]),
        'second': float_or_none(row["DAY"]),
        'focal_depth': float_or_none(row['FOCAL_DEPTH']),
        'magnitude': float_or_none(row['EQ_MAG_MW']),
        'intensity': float_or_none(row['INTENSITY']),
        'deaths': int_or_none(row["DEATHS"]),
        'missing': int_or_none(row["MISSING"]),
        'damage': float_or_none(row["DAMAGE_MILLIONS_DOLLARS"]),
        'houses_destroyed': int_or_none(row['HOUSES_DESTROYED']),
        'houses_damaged': int_or_none(row['HOUSES_DAMAGED']),
        'total_deaths': int_or_none(row["TOTAL_DEATHS"]),
        'total_missing': int_or_none(row["TOTAL_MISSING"]),
        'total_damage': float_or_none(row["TOTAL_DAMAGE_MILLIONS_DOLLARS"]),
        'total_houses_destroyed': int_or_none(row['TOTAL_HOUSES_DESTROYED']),
        'total_houses_damaged': int_or_none(row['TOTAL_HOUSES_DAMAGED'])
    }


if __name__ == '__main__':
    results = requests.get(
        "https://www.ngdc.noaa.gov/nndc/struts/results?type_0=Exact&query_0=$ID&t=101650&s=13&d=189&dfn=signif.txt")

    engine = create_engine(configs.DB_URL, echo=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    f = StringIO(results.text)
    reader = csv.DictReader(f, delimiter='\t')
    rows = [row for row in reader]

    earthquakes = [format_row(row) for row in rows]
    print(earthquakes)

    session.add_all([models.Earthquake(**row) for row in earthquakes])
    session.commit()
