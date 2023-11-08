# FIO REST API endpoints

FIO Wrapper includes the most commonly used FIO REST API endpoints.

## Building
- `GET` /building/{BuildingTicker}
- `GET` /building/allbuildings

## Exchange
- `GET` /exchange/{ExchangeTicker}
- `GET` /exchange/all
- `GET` /exchange/full
- `GET` /exchange/orders/{CompanyCode}
- `GET` /exchange/orders/{CompanyCode}/{ExchangeCode}

## LocalMarket
- `GET` /localmarket/planet/{Planet}
- `GET` /localmarket/planet/{Planet}/{Type}
- `GET` /localmarket/shipping/source/{Planet}
- `GET` /localmarket/shipping/destination/{Planet}
- `GET` /localmarket/company/{Company}

## Material
- `GET` /material/{MaterialTicker}
- `GET` /material/allmaterials
- `GET` /material/category/{CategoryName}

## Planet

- `GET` /planet/{Planet}
- `GET` /planet/allplanets
- `GET` /planet/allplanets/full
- `GET` /planet/sites/{Planet}
- `POST` /planet/search

## Recipes
- `GET` /recipes/{Ticker}
- `GET` /recipes/allrecipes

## Sites

- `GET` /sites/{UserName}
- `GET` /sites/planets/{UserName}
- `GET` /sites/{UserName}/{Planet}
- `GET` /sites/warehouses/{UserName}

## Storage

- `GET` /storage/{UserName}
- `GET` /storage/planets/{UserName}
- `GET` /storage/{UserName}/{StorageDescription}

## Group

- `GET` /auth/groups
- `GET` /auth/group/{GroupId}
- `GET` /auth/groupmemberships
- `POST` /fioweb/grouphub
- `GET` /fioweb/burn/group/{GroupId}