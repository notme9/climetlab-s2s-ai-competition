import xarray as xr
import climetlab as cml

version = '0.0.9'

def test_merge_2020_01_02_and_2020_01_09():
    merge_multiple_dates(["20200102", "20200109"])


def test_merge_2020_01_02():
    merge("20200102")


def test_merge_2020_12_31():
    merge("20201231")


def merge(date):

    dslist = []
    ds = cml.load_dataset("s2s-ai-competition", date=date, parameter="2t", version=version)
    dslist.append(ds.to_xarray())
    ds = cml.load_dataset("s2s-ai-competition", date=date, parameter="tp", version=version)
    dslist.append(ds.to_xarray())

    def check(ds):

        print(dict(ds.dims), list(ds.keys()))

    for ds in dslist:
        check(ds)

    ds = xr.merge(dslist)
    print("-- Merged into --")
    check(ds)

    dslist[0].step.values, dslist[1].step.values


def merge_multiple_dates(dates):

    dslist = []
    for date in dates:
        ds = cml.load_dataset("s2s-ai-competition", date=date, parameter="2t", version=version)
        dslist.append(ds.to_xarray())

    def check(ds):

        print(dict(ds.dims), list(ds.keys()))

    for ds in dslist:
        check(ds)

    ds = xr.merge(dslist)
    print("-- Merged into --")
    check(ds)


if __name__ == "__main__":
    merge_multiple_dates(["20200102", "20200109"])
    merge("20200102")
    merge("20201231")
