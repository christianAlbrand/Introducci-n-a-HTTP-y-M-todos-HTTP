from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Producto


def obtener_productos(request):
    if request.method == "GET":
        productos = list(Producto.objects.values())
        return JsonResponse(productos, safe=False, status=200)

    return JsonResponse(
        {"error": "Método no permitido"},
        status=405
    )


@csrf_exempt
def crear_producto(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            Producto.objects.create(
                nombre=data["nombre"],
                cantidad=data["cantidad"],
                precio=data["precio"]
            )

            return JsonResponse(
                {"mensaje": "Producto creado"},
                status=201
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "JSON inválido"},
                status=400
            )

        except KeyError as e:
            return JsonResponse(
                {"error": f"Falta el campo {str(e)}"},
                status=400
            )

    return JsonResponse(
        {"error": "Método no permitido"},
        status=405
    )


@csrf_exempt
def actualizar_producto(request, id):
    if request.method != "PUT":
        return JsonResponse(
            {"error": "Método no permitido"},
            status=405
        )

    if not request.body:
        return JsonResponse(
            {"error": "El cuerpo de la petición está vacío"},
            status=400
        )

    try:
        data = json.loads(request.body.decode("utf-8"))
        producto = Producto.objects.get(id=id)

        producto.nombre = data.get("nombre", producto.nombre)
        producto.cantidad = data.get("cantidad", producto.cantidad)
        producto.precio = data.get("precio", producto.precio)
        producto.save()

        return JsonResponse(
            {"mensaje": "Producto actualizado"},
            status=200
        )

    except Producto.DoesNotExist:
        return JsonResponse(
            {"error": "Producto no encontrado"},
            status=404
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "JSON inválido"},
            status=400
        )


@csrf_exempt
def eliminar_producto(request, id):
    if request.method == "DELETE":
        try:
            producto = Producto.objects.get(id=id)
            producto.delete()

            return JsonResponse(
                {"mensaje": "Producto eliminado"},
                status=200
            )

        except Producto.DoesNotExist:
            return JsonResponse(
                {"error": "Producto no encontrado"},
                status=404
            )

    return JsonResponse(
        {"error": "Método no permitido"},
        status=405
    )