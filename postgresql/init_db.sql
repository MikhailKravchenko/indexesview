create table price
(
    price_id   serial
        constraint price_pk
            primary key,
    market     varchar(100),
    name_coin  varchar(100),
    price      double precision,
    created_at timestamp default now(),
    update_at  timestamp default now()
);

alter table price
    owner to indexesview;

create unique index price_market_name_coin_uindex
    on price (market, name_coin);

