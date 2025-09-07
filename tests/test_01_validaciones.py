from importlib.machinery import SourceFileLoader

mod = SourceFileLoader("m", "src/01_validaciones.py").load_module()

def test_es_texto_vacio():
    assert mod.es_texto_vacio("") is True
    assert mod.es_texto_vacio("   ") is True
    assert mod.es_texto_vacio("hola") is False
