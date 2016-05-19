#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
con = lite.connect('pos_empresa.db')

c = con.execute("SELECT COUNT(*) FROM sale WHERE date LIKE \"2013%\"")
for row in c:
 	print"Cantidad total de ventas en el anio 2013", row[0]
 

print("¿Precio promedio de venta por producto?")
print

c = con.execute("SELECT product.name, AVG(sale_product.net_unit_price) FROM sale_product JOIN product ON product.id = sale_product.product_id GROUP BY product_id LIMIT 5")
for row in c:
 	print "Producto: ",row[0]
 	print "Promedio Venta: ",row[1]
 	print "-----"
 
print "Total de ventas por cliente:"
 
c = con.execute("SELECT entity.names, entity.surnames, entity.company_name, SUM(sale.gross_total) AS total_ventas FROM sale JOIN entity ON sale.entity_id = entity.id GROUP BY sale.entity_id LIMIT 5")
for row in c:
 	print "Nombre: ",row[0]
 	print "Apellido: ",row[1]
 	print "Nombre Empresa: ",row[2]
 	print "T.ventas: ",str(row[3])
 	print "------"

print "Total de ventas por cliente el año 2014:"
c = con.execute("SELECT entity.names, entity.surnames, entity.company_name, SUM(sale.gross_total) AS total_ventas FROM sale JOIN entity ON sale.entity_id = entity.id WHERE date LIKE \"2014%\" GROUP BY sale.entity_id LIMIT 5")
for row in c:
 	print "Nombre: ",row[0]
 	print "Apellido: ",row[1]
 	print "Nombre empresa: ",row[2]
 	print "Total ventas: ",str(row[3])
 	print "----"
 

print "Total de ventas por fecha en noviembre del 2013:"
c = con.execute("SELECT date, COUNT(*), SUM(gross_total) FROM sale WHERE date LIKE \"2013-11%\" GROUP BY date;")
for row in c:
 	print "Fecha: ",row[0]
 	print "Cantidad de ventas: ",row[1]
 	print "T.ventas: ",row[2]
 	print "-----"
 
print "Cantidad y montos totales por producto:"
c = con.execute("SELECT product.name, sale_product.quantity, sale_product.gross_total FROM sale_product JOIN product ON sale_product.product_id = product.id ORDER BY sale_product.quantity DESC LIMIT 5;")
for row in c:
 	print "Producto: ",row[0]
 	print "cantidad: ",row[1]
 	print "T.ventas: ",row[2]
 	print "-----"

 
