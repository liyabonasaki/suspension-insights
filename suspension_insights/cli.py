import click
import time
from datetime import datetime
from suspension_insights.repository import read_payments
from suspension_insights.service import generate_reports

@click.command()
@click.argument('input_file')
@click.argument('output_folder')
def main(input_file, output_folder):
    try:
        print("building reports ....")
        reference_date = datetime.today()
        payments = read_payments(input_file)
        generate_reports(payments, output_folder, reference_date)
        time.sleep(2)
        print("done building reports")
    except:
        print("failed to buid reports")

if __name__ == "__main__":
    main()