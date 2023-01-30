import sentry_sdk

sentry_sdk.init(
    dsn='https://e1becb71961e4be8893a9a2a8c847281@o4504562589564928.ingest.sentry.io/4504591390801920',
    traces_sample_rate=1.0
)


def main():
    print('main')


if __name__ == '__main__':
    main()
