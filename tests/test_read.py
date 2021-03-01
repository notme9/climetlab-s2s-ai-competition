#!/usr/bin/env python3

# (C) Copyright 2020 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import climetlab as cml

# import climetlab_s2s_ai_competition
# from climetlab_s2s_ai_competition.source import S2sReferenceDataSource
# import climetlab_s2s_ai_competition as addon


def test_read_rt_tp_and_2t():
    ds = cml.load_dataset("s2s-ai-competition", date="20200102", parameter=["tp", "2t"])
    xds = ds.to_xarray()
    print(xds)


def test_read_rt():
    ds = cml.load_dataset("s2s-ai-competition", date="20200102")
    xds = ds.to_xarray()
    print(xds)

    sst = xds.sel()


# cml.plot_map(ds) # does not work


def test_read_hc():
    ds = cml.load_dataset("s2s-ai-competition", date="20200102", hindcast=True)
    xds = ds.to_xarray()
    print(xds)


def test_read_rt_2dates():
    ds = cml.load_dataset("s2s-ai-competition", date=["20200102", "20200102"])
    xds = ds.to_xarray()
    print(xds)

    sst = xds.sel()


if __name__ == "__main__":
    test_read_rt()
    # test_read_hc() # not uploaded yet
