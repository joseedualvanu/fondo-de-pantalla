"""
MODULO B
    Description: get the sales from snowflake

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

def b_snow(direction,log_name,file_keyP8):
    log_file = open(log_name, 'a')
    log_file.write('B - Snowflake\n')
    print('B - Snowflake')
    log_file.close()

    from A_Email_error import enviar_mail_error
    from snowflake import connector
    import sys

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.asymmetric import dsa
    from cryptography.hazmat.primitives import serialization

    try:
            with open(file_keyP8, "rb") as key:
                p_key= serialization.load_pem_private_key(
                    key.read(),
                    # password=os.environ["Tata2"].encode(),
                    password=None,
                    backend=default_backend()
                )

            pkb = p_key.private_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption())

            conn = connector.connect(
                user='',
                account='',
                private_key= pkb,
                warehouse='',
                database='',
                schema=''
                )

            #create cursor
            curs = conn.cursor()

    except:
        print('The conexion in Snowflake couldnt be made')
        log_file = open(log_name, 'a')
        log_file.write('The conexion in Snowflake couldnt be made\n')
        log_file.write('-------------------------------------\n')
        log_file.close()
        enviar_mail_error(log_name)
        sys.exit()

    sql1 = '''
    Consulta SQL
    '''

    try:
        curs.execute(sql1)
    except:
        print('Problem with the execution of the sql in Snowflake')
        log_file = open(log_name, 'a')
        log_file.write('Problem with the execution of the sql in snowflake\n')
        log_file.write(str(curs)+'\n')
        log_file.write('-------------------------------------\n')
        log_file.close()
        curs.close()
        enviar_mail_error(log_name)
        sys.exit()

    df = curs.fetch_pandas_all()

    # Cierro la conexion
    curs.close()

    amount = int(df["SUM (AHORRO)"][0])
    days = int(df["CANT_DIAS"][0])
    amount_day = int(round(amount/days,0))

    # Format with comma
    amount = format(amount, ',d')
    amount_day = format(amount_day, ',d')

    return amount,days,amount_day
