from kerapu.application.KerapuApplication import KerapuApplication


def main():
    application = KerapuApplication()
    status = application.run()

    exit(status)
