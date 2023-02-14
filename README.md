# Django Serverside Datatable
[Downloads]https://pypi.org/project/Serverside-tables-django-framework/


Este es un paquete simple que le permite usar Datatable del lado del servidor en su proyecto Django

Admite funciones de tabla de datos como paginación, búsqueda, etc.

## Instalar

```
pip install django-serverside-datatable-post
```


## Cómo utilizar

Create a django View that inherits from  **ServerSideDatatablePostView**.
```
Ejemplo (backend):

```
python
# views.py

from django_serverside_datatable_post.views import ServerSideDatatablePostView


class ItemListView(ServerSideDatatablePostView):
	queryset = models.Item.objects.all()
	columns = ['nombre', 'codigo', 'descripcion']


# urls.py
# agregue la siguiente línea a urlpatterns

path('data/', views.ItemListView.as_view(), name='url_test'), 

```

Ejemplo (frontend):

```
html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
	</head>
	<body>
		<h1>Items</h1>
		<hr>
		<table id="items-table">
			<thead>
				<tr>
					<th>Nombre</th>
					<th>Codigo</th>
					<th>Descripciion</th>
				</tr>
			</thead>
			<tbody></tbody>
		</table>

		<script src="https://code.jquery.com/jquery-3.6.3.js" integrity="sha256-nQLuAZGRRcILA+6dMBOvcRh5Pe310sBpanc6+QBmyVM=" crossorigin="anonymous"></script>
		<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
		<script language="javascript">
			$(document).ready(function () {
				$('#items-table').dataTable({
					serverSide: true,
					sAjaxSource: "{% url 'url_test' %}",  // Agregar url
					sServerMethod: "POST", // se establece el metodo POST
					columns: [
						{name: "nombre", data: 0},
						{name: "codigo", data: 1},
						{name: "descripcion", data: 2},
					],
				});
			});
		</script>
	</body>
</html>
```

Para una mayor personalización de Datatable, puede consultar la documentación oficial de Datatable.
