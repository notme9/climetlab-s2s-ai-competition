# (C) Copyright 2020 ECMWF.  #
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import math
import xarray as xr
import numpy as np

# note this version number has nothing to do with the version number of the dataset
__version__ = "0.2.0"

import climetlab as cml
from climetlab import Dataset


def _makelist(x):
    if isinstance(x, list):
        return x
    elif isinstance(x, tuple):
        return list(x)
    else:
        return [x]


URL = "https://storage.ecmwf.europeanweather.cloud"
DATA = "s2s-ai-competition/data"
PATTERN = (
    "{url}/{data}/{dataset}/{version}/{format}/{parameter}-{fctype}-{date}.{extension}"
)
ZARRPATTERN = (
    "{url}/{data}/{dataset}/{version}/{format}/{fctype}-{date}.{extension}"
)
# this is the default version of the dataset
VERSION = "0.1.7"


class S2sDataset(Dataset):
    name = None
    home_page = "-"
    licence = "https://apps.ecmwf.int/datasets/data/s2s/licence/"
    # TODO : upload a json file next to the dataset and read it
    documentation = "-"
    citation = "-"

    terms_of_use = ("By downloading data from this dataset, you agree to the their terms: "
    "Attribution 4.0 International(CC BY 4.0). If you do not agree with such terms, "
    "do not download the data. For more information, please visit https://www.ecmwf.int/en/terms-use "
    "and https://apps.ecmwf.int/datasets/data/s2s/licence/.")

    dataset = None

    def __init__(self):
        pass

    def _load(self, *args, **kwargs):
        format = kwargs.pop("format", "grib")
        load = getattr(self, f"_load_{format}")
        return load(*args, **kwargs)

    def _make_request(
        self,
        date=None,
        parameter="tp",
        hindcast=False,
        version=VERSION,
    ):
        request = dict(
            url=URL,
            data=DATA,
            dataset=self.dataset,
            version=version,
            parameter=parameter,
            fctype="hc" if hindcast else "rt",
            date=date,
        )
        return request

    def _load_grib(self, *args, **kwargs):
        request = self._make_request(*args, **kwargs)
        request["format"] = "grib"
        request["extension"] = "grib"
        self.source = cml.load_source("url-pattern", PATTERN, request)

    def _load_netcdf(self, *args, **kwargs):
        request = self._make_request(*args, **kwargs)
        request["format"] = "netcdf"
        request["extension"] = "nc"
        self.source = cml.load_source("url-pattern", PATTERN, request)

    def _load_zarr(self, *args, **kwargs):

        from climetlab.utils.patterns import Pattern
        from climetlab.sources.url import Url

        request = self._make_request(*args, **kwargs)
        request["format"] = "zarr"
        request["extension"] = "zarr"
        request.pop('parameter')

        urls = Pattern(ZARRPATTERN).substitute(request)
        if not isinstance(urls, list):
            urls = [urls]

        url = urls[0]
        self.source = cml.load_source("zarr-s3", urls)
