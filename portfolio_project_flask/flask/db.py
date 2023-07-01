import psycopg2


conn = psycopg2.connect(
    """ 
    dbname=portfolioflask user=postgres host=localhost port=5432
    """
)