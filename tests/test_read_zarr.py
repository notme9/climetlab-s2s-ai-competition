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


def test_read_zarr():
    ds = cml.load_dataset("s2s-ai-competition", version='0.1.7', format='zarr')
    xds = ds.to_xarray()
    print(xds)


if __name__ == "__main__":
#    test_direct_read_zarr()
    test_read_zarr()
