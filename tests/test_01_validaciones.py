from importlib.machinery import SourceFileLoader

mod = SourceFileLoader("m", "src/01_validaciones.py").load_module()
es_texto_vacio = mod.es_texto_vacio

def test_es_texto_vacio():
    assert es_texto_vacio("") is True
    assert es_texto_vacio("   ") is True
    assert es_texto_vacio("hola") is False
