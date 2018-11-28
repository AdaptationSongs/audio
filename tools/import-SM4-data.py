#!/usr/bin/python
"""
Tool to parse data from Wildlife Acoustics SM4 log files
Output is stored in the specified database.

Arguments: [database URI] [CSV file]

Copyright (c) Damian Christey
License: GPL
"""

import sys
import csv
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class sm4_data(Base):
    # Set up table and columns
    __tablename__ = 'sm4_data'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    sn = Column(Text(255))
    timestamp = Column(DateTime)
    lat = Column(Float)
    lon = Column(Float)
    volts = Column(Float)
    temp = Column(Float)
    num_files = Column(Integer)
    mic0 = Column(Text(15))
    mic1 = Column(Text(15))

# Create the database
engine = create_engine(sys.argv[1])
Base.metadata.create_all(engine)

# Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

sn = sys.argv[2].split('_')[0]

# Read the txt file as CSV
with open(sys.argv[2], 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    try:
        t = time()
        imported = 0
        existing = 0
        for row in reader:
            # skip over header rows
            if (row[0] != 'DATE'):
                record = sm4_data(**{
                    'sn' : sn,
                    'timestamp' : datetime.strptime(row[0]+' '+row[1],
                                                    '%Y-%b-%d %H:%M:%S'),
                    'lat' : row[2],
                    'lon' : row[4],
                    'volts': row[6],
                    'temp': row[7],
                    'num_files': row[8],
                    'mic0': row[9],
                    'mic1': row[10]
                })
                # search for matching records
                match = s.query(sm4_data).filter(
                    sm4_data.sn == record.sn,
                    sm4_data.timestamp == record.timestamp
                )
                if (match.count() > 0):
                     # Skip over existing records
                    existing += 1
                else:
                    # Add new record to the session
                    s.add(record)
                    imported += 1

        s.commit() # Attempt to commit all the records

    except Exception as e:
        print('Something bad happened: {0}'.format(e))
        s.rollback() # Rollback the changes on error

    finally:
        s.close() # Close the connection
        print('Imported rows: {0}'.format(imported))
        print('Existing records skipped: {0}'.format(existing))
        print('Time elapsed: {0} seconds'.format(time() - t))
