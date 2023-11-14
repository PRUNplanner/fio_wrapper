# Config

## Base Configuration

```ini
[FIO]
application = FIO Wrapper
version = 1.0.0
base_url = https://rest.fnar.net
timeout = 10
ssl_verify = True
versions = 1.0.0

[URL]
# material
1.0.0_material_base = /material
1.0.0_material_all = /allmaterials

# exchange
1.0.0_exchange_base = /exchange
1.0.0_exchange_orders = /orders
1.0.0_exchange_all = /all
1.0.0_exchange_full = /full

# building
1.0.0_building_base = /building
1.0.0_building_all = /allbuildings

# recipe
1.0.0_recipe_base = /recipes
1.0.0_recipe_all = /allrecipes

# planet
1.0.0_planet_base = /planet
1.0.0_planet_all = /allplanets
1.0.0_planet_full = /allplanets/full
1.0.0_planet_sites = /sites
1.0.0_planet_search = /search

# localmarket
1.0.0_localmarket_base = /localmarket
1.0.0_localmarket_planet = /planet
1.0.0_localmarket_shipping_source = /shipping/source
1.0.0_localmarket_shipping_destination = /shipping/destination
1.0.0_localmarket_company = /company

# sites
1.0.0_sites_base = /sites
1.0.0_sites_planets = /planets
1.0.0_sites_warehouses = /warehouses

# storage
1.0.0_storage_base = /storage
1.0.0_storage_planets = /planets

# groups
1.0.0_groups = /auth/groups
1.0.0_groups_group = /auth/group
1.0.0_groups_groupmemberships = /auth/groupmemberships
1.0.0_groups_hub = /fioweb/grouphub
1.0.0_groups_burn = /fioweb/burn/group
```

## Config() class
::: config