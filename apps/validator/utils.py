import datetime
import re

from django.core.exceptions import ValidationError


class NumberPhone:
    @classmethod
    def valide_cellphone(cls, cellphone):
        expression_regular_cellphone = "^(^\+593|^593|^0)?9\d{8}$"  # noqa W605
        expression_regular_phone = (
            "^(^\+|^07|^06|^05|^04|^03|^2|^3|\))?[2,3]\d{6}$"  # noqa W605
        )
        if cellphone is not None:
            if len(str(cellphone)) >= 8:
                if re.match(expression_regular_cellphone, str(cellphone)) is not None:
                    return cellphone
        else:
            if re.match(expression_regular_phone, str(cellphone)) is not None:
                return ""
        raise ValidationError("Introduzca una número de teléfono válida.")

class ValidatorDateTime:
    @classmethod
    def validate_future_date(cls, value):
        if value <= datetime.date.today():
            raise ValidationError("La fecha debe ser mayor que la fecha actual.")

class TypeDocument:
    @classmethod
    def valide_ruc(cls, ruc):
        if len(ruc) != 10 and len(ruc) != 13:
            raise ValidationError("Introduzca una número de RUC válida.")
        if len(ruc) == 10:
            # RUC de persona natural
            province = int(ruc[:2])
            if province < 1 or province > 24:
                raise ValidationError("Introduzca una número de RUC válida.")
            third_digit = int(ruc[2])
            if third_digit < 0 or third_digit > 9:
                raise ValidationError("Introduzca una número de RUC válida.")
            # Los siete siguientes dígitos pueden ser cualquier número
            # Calcular dígito verificador
            sum = 0
            for i in range(9):
                sum += int(ruc[i]) * (i + 2)
            residue = sum % 11
            check_digit = 11 - residue if residue != 0 else 0
            return int(ruc[9]) == check_digit
        elif len(ruc) == 13:
            # RUC de empresa o entidad legal
            province = int(ruc[:3])
            if province < 1 or province > 24:
                raise ValidationError("Introduzca una número de RUC válida.")
            # Los nueve siguientes dígitos pueden ser cualquier número
            # Calcular dígito verificador
            sum = 0
            for i in range(9):
                sum += int(ruc[i]) * (i + 2)
            residue = sum % 11
            digito_verificador = 11 - residue if residue != 0 else 0
            return int(ruc[9]) == digito_verificador