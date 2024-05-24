# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import mysql.connector

@csrf_exempt
def add_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_number = data.get('room')

            # MySQLに接続
            connection = mysql.connector.connect(
                host='172.34.0.6',
                user='test',
                password='test',
                database='test_db'
            )
            cursor = connection.cursor()

            # INSERT文を実行
            sql = f"""
                INSERT INTO
                    t_nurse_call (room_no, status)
                VALUES
                    (\"{room_number}\", "ready");
            """
            cursor.execute(sql)
            print(sql)
            connection.commit()

            cursor.close()
            connection.close()

            return JsonResponse({'status': 'success', 'room_number': room_number})
        except Exception as e:
            print(e)
            print(f"sql:{sql}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def select_tables(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_number = data.get('room')

            # MySQLに接続
            connection = mysql.connector.connect(
                host='172.34.0.6',
                user='test',
                password='test',
                database='test_db'
            )
            cursor = connection.cursor(dictionary=True)

            # SELECT文を実行
            sql = f"""
                SELECT
                    *
                FROM
                    t_nurse_call
                WHERE
                    status IN ('ready', 'work');
            """

            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            connection.commit()

            cursor.close()
            connection.close()

            return JsonResponse({'status': 'success', 'data': data})
            # return data
        except Exception as e:
            print(e)
            print(f"sql:{sql}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def update_ready_to_work(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            # MySQLに接続
            connection = mysql.connector.connect(
                host='172.34.0.6',
                user='test',
                password='test',
                database='test_db'
            )
            cursor = connection.cursor(dictionary=True)

            # SELECT文を実行
            sql = f"""
                UPDATE
                    t_nurse_call
                SET
                    status = 'work'
                WHERE
                    status = 'ready'
                    AND id = {id};
            """

            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            connection.commit()

            cursor.close()
            connection.close()

            return JsonResponse({'status': 'success', 'data': data})
            # return data
        except Exception as e:
            print(e)
            print(f"sql:{sql}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def update_work_to_done(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            # MySQLに接続
            connection = mysql.connector.connect(
                host='172.34.0.6',
                user='test',
                password='test',
                database='test_db'
            )
            cursor = connection.cursor(dictionary=True)

            # SELECT文を実行
            sql = f"""
                UPDATE
                    t_nurse_call
                SET
                    status = 'done'
                WHERE
                    status = 'work'
                    AND id = {id};
            """

            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            connection.commit()

            cursor.close()
            connection.close()

            return JsonResponse({'status': 'success', 'data': data})
            # return data
        except Exception as e:
            print(e)
            print(f"sql:{sql}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def update_status_to_ready(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            # MySQLに接続
            connection = mysql.connector.connect(
                host='172.34.0.6',
                user='test',
                password='test',
                database='test_db'
            )
            cursor = connection.cursor(dictionary=True)

            # SELECT文を実行
            sql = f"""
                UPDATE
                    t_nurse_call
                SET
                    status = 'ready'
                WHERE
                    AND id = {id};
            """

            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            connection.commit()

            cursor.close()
            connection.close()

            return JsonResponse({'status': 'success', 'data': data})
            # return data
        except Exception as e:
            print(e)
            print(f"sql:{sql}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def update_status_to_clear(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')

            # MySQLに接続
            connection = mysql.connector.connect(
                host='172.34.0.6',
                user='test',
                password='test',
                database='test_db'
            )
            cursor = connection.cursor(dictionary=True)

            # SELECT文を実行
            sql = f"""
                UPDATE
                    t_nurse_call
                SET
                    status = 'clear'
            """

            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            connection.commit()

            cursor.close()
            connection.close()

            return JsonResponse({'status': 'success', 'data': data})
            # return data
        except Exception as e:
            print(e)
            print(f"sql:{sql}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
