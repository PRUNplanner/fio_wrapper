# Group 
Exposes FIO group data. All Group data requires a `FIO API KEY`. You will need to have access to the data the user has in FIO in order to access it.

Groups can be created and modified in the [FIO Settings](https://fio.fnar.net/settings).

## Examples
### All groups & their information

```python
# Get all groups 
groups = fio.Group.all()

# Iterate through group IDs and print group details
for id in groups.ids():
    # Get information of specific group by Id
    group = fio.Group.get(groupid=id)
    print(group)
```

### Members of a specific Group and Hub information
```python
# Get group users
group_user = fio.Group.get(groupid=123456).users()

# Get hub information
data = fio.Group.hub(group_user)
```

### Members Burn information
```python
# Get Burn information
data = fio.Group.burn(groupid=123456)
```

## Endpoints

::: endpoints.endpoints_v1.group