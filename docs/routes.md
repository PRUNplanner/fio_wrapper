# FIO REST API endpoints

FIO Wrapper includes the most commonly used FIO REST API endpoints.

## Planet

- `GET` /planet/{Planet}
- `GET` /planet/allplanets
- `GET` /planet/allplanets/full
- `GET` /planet/sites/{Planet}
- `POST` /planet/search

## Material
- `GET` /material/{MaterialTicker}
- `GET` /material/allmaterials
- `GET` /material/category/{CategoryName}

## Building
- `GET` /building/{BuildingTicker}
- `GET` /building/allbuildings

## Recipes
- `GET` /recipes/{Ticker}
- `GET` /recipes/allrecipes

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

