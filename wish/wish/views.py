from django.http import HttpResponse
import sqlite3, os
from wish.settings import BASE_DIR


from django.views.decorators.csrf import csrf_exempt
import json,datetime
from django import template

register = template.Library()

@register.filter
def percentage(value):
    return format(value, "%")

def gen():
    m = -1
    while True:
        m+=1
        yield m

def gen2():
    m = 0
    while True:
        m+=1
        yield m


@csrf_exempt
def dbInterface(request,input):
	keys = ''
	values = ''
	listTable = 'list'
	bankTable = 'bank'
	if request.method == 'GET':
		post = request.GET
		if input=='add':
			for i in ['sku']:
				values+="'"+str(post.get(i,False))+"',"
				keys+=i+','
			connection = sqlite3.connect(os.path.join(BASE_DIR,'db.sqlite3'))
			cursor = connection.cursor()
			ret = 'Successfully added item to your wishlist!'
			listTable+='_'+str(post['id'])
			num = 0
			cursor.execute("SELECT COUNT(*) from %s"%listTable)
			for data in cursor.fetchall():num = int(data[0])
			if num>=10:
				ret = 'You have exceeded the limit in wishlist. Kindly delete old items to make room for new ones.'
			else:
				try:
					print("SELECT emi from %s where %s = %s"%(bankTable,'sku',post.get('sku',False)))
					cursor.execute("SELECT emi from %s where %s = %s"%(bankTable,'sku',post.get('sku',False)))
					values+="'"+str(cursor.fetchall()[0][0])+"',"
					keys+='emi,'
					values+="'"+str(datetime.datetime.now())+"'"
					keys+='time'
					print("INSERT INTO %s (%s) values (%s) "%(listTable,keys,values))
					cursor.execute("INSERT INTO %s (%s) values (%s) "%(listTable,keys,values))
				except:
					ret = 'Item already present in your wishlist.'
			connection.commit()
			return HttpResponse(json.dumps({'message':ret}),content_type="application/json")
		elif input=='bank':
			for i in ['sku','name','url','emi','months']:
				values+="'"+str(post.get(i,False))+"',"
				keys+=i+','
			connection = sqlite3.connect(os.path.join(BASE_DIR,'db.sqlite3'))
			cursor = connection.cursor()
			ret = 'Successfully added new product!'
			num = 0
			try:
				print("INSERT INTO %s (%s) values (%s) "%(bankTable,keys,values))
				cursor.execute("INSERT INTO %s (%s) values (%s) "%(bankTable,keys,values))
			except:
				ret = 'Product already present in the database.'
			connection.commit()
			return HttpResponse(json.dumps({'message':ret}),content_type="application/json")
		elif input=='auto':
		    if post['name']=="":return HttpResponse(json.dumps([]),content_type="application/json")
		    else:
		        for i in ['name']:values+="'"+post.get(i,False)+"',";keys+=i+','
		        connection = sqlite3.connect(os.path.join(BASE_DIR,'db.sqlite3'))
		        cursor = connection.cursor()
		        ret = []
		        fields = ['id','sku','name','url','emi','months']
		        try:
		            print("SELECT * from %s where name like %s"%('bank','"'+post['name']+'%"'))
		            cursor.execute("SELECT * from %s where name like %s"%('bank','"'+post['name']+'%"'))
		            myNum = gen()
		            for data in cursor.fetchall():ret.append({next(myNum):dict(zip(fields,data))})
		        except:ret = [{'':''}]
		        connection.commit()
		    return HttpResponse(json.dumps(ret),content_type="application/json")
		elif input=='read':
		    if post['id']=="":return HttpResponse(json.dumps([]),content_type="application/json")
		    else:
		        for i in ['id']:values+="'"+post.get(i,False)+"',";keys+=i+','
		        connection = sqlite3.connect(os.path.join(BASE_DIR,'db.sqlite3'))
		        cursor = connection.cursor()
		        try:
		            ret = []
		            fields = ['index','sku','name','url','emi','months']
		            print("SELECT * from %s"%('list_'+post['id']))
		            cursor.execute("SELECT * from %s"%('list_'+post['id']))
		            myNum = gen2()
		            for data in cursor.fetchall():ret.append({next(myNum):dict(zip(fields,data))})
		        except:ret = [{'':''}]
		        connection.commit()
		    return HttpResponse(json.dumps(ret),content_type="application/json")
		elif input=='delete':
		    connection = sqlite3.connect(os.path.join(BASE_DIR,'db.sqlite3'))
		    cursor = connection.cursor()
		    cursor.execute("SELECT * from %s where sku = %s"%('list_'+post['id'],post['sku']))
		    all = cursor.fetchall()
		    if len(all)>0:
		        try: cursor.execute("DELETE from %s where sku = %s"%('list_'+post['id'],post['sku'])); ret = 'Item removed from your wishlist.'
		        except : ret = 'Failed to remove the item from your wishlist. Try again.'
		    else: ret = 'Item not present in your wishlist anymore'
		    connection.commit()
		    return HttpResponse(json.dumps({'message':ret}),content_type="application/json")
		else:
		    return HttpResponse('404 : Prafulla not found')

@csrf_exempt
def add(req):
    return dbInterface(req,'add')

@csrf_exempt
def auto(req):
    return dbInterface(req,'auto')

@csrf_exempt
def bank(req):
    return dbInterface(req,'bank')

@csrf_exempt
def delete(req):
    return dbInterface(req,'delete')

@csrf_exempt
def read(req):
    return dbInterface(req,'read')


