sensors = [
    {
        'model' : 'Acurite-Tower',
        'id' : 5754,
        'interval' : 60,
        'max_temp_delta' : 2,
        'feed' : 'acurite.a',
        'battery_feed' : 'acurite.a-bat'
    },
    {
        'model' : 'Acurite-Tower',
        'id' : 8136,
        'interval' : 60,
        'max_temp_delta' : 2,
        'feed' : 'acurite.b',
        'humidity_feed' : 'acurite.b-hum',
        'battery_feed' : 'acurite.b-bat'
    },
    {
        'model' : 'Acurite-Tower',
        'id' : 11161,
        'interval' : 60,
        'max_temp_delta' : 2,
        'feed' : 'acurite.c',
        'humidity_feed' : 'acurite.c-hum',
        'battery_feed' : 'acurite.c-bat'
    },
    {
        'model' : 'Acurite-606TX',
        'id' : 6,
        'interval' : 60,
        'max_temp_delta' : 2,
        'feed' : 'acurite.606tx',
        'battery_feed' : 'acurite.606tx-bat'
    },
    {
        'model' : 'Acurite-Tower',
        'id' : 8252,
        'interval' : 60,
        'max_temp_delta' : 2,
        'feed' : 'acurite.shop',
        'humidity_feed' : 'acurite.shop-hum',
        'battery_feed' : 'acurite.shop-bat'
    }
]

secrets = {
    'aio_username' : '{ADAFRUIT_IO_USERNAME}',
    'aio_key' : '{ADAFRUIT_IO_KEY}',
    }
