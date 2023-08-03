# Depicting namespace packages

This contains 2 namespace packages in the packages directory:

1. billups-date-utils
1. billups-magic-numbers

## Installing

Individual packages can be installed as follows:

```
pip install "billups-date-utils @ git+ssh://git@github.com/kehindeadewusi/rps/#subdirectory=packages/billups-date-utils"
```

and for the second package

```
pip install "billups-magic-numbers @ git+ssh://git@github.com/kehindeadewusi/rps/#subdirectory=packages/billups-magic-numbers"
```

## Testing

You can run the service project to test, after installing:

```
python3 billups-service/billups_service.py
```
