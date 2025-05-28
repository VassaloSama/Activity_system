import unittest
import requests

class TestAtividadesAPI(unittest.TestCase):

    def setUp(self):
        self.school_url = 'http://localhost:5000'
        self.base_url = "http://localhost:5002"

    def criar_professor(self, id=1):
        return requests.post(f'{self.school_url}/professores', json={
            'id': id,
            'nome': 'fernando',
            'idade': 27,
            'materia': 'matematica',
            'observacoes': 'professor de matematica muito profissional'
        })

    def test_00_resetar_dados(self):
        r2 = requests.post(f"{self.base_url}/atividades/resetar")
        r1 = requests.post(f'{self.school_url}/resetar')
        self.assertEqual(r2.status_code, 200)
        self.assertEqual(r1.status_code, 200)

    def test_01_criar_atividade_valida(self):
        self.criar_professor(id=1)
        dados = {
            "atividade_id": 1,
            "professor_id": 1,
            "enunciado": "Resolver equação de 2º grau"
        }
        response = requests.post(f"{self.base_url}/atividades", json=dados)
        self.assertEqual(response.status_code, 201)

    def test_02_criar_atividade_com_id_existente(self):
        dados = {
            "atividade_id": 1,
            "professor_id": 1,
            "enunciado": "Atividade duplicada"
        }
        response = requests.post(f"{self.base_url}/atividades", json=dados)
        self.assertEqual(response.status_code, 400)

    def test_03_listar_atividades(self):
        response = requests.get(f"{self.base_url}/atividades")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_04_obter_atividade_por_id(self):
        response = requests.get(f"{self.base_url}/atividades/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['atividade_id'], 1)

    def test_05_atualizar_atividade_existente(self):
        dados = {"enunciado": "Novo enunciado atualizado"}
        response = requests.put(f"{self.base_url}/atividades/1", json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Atividade atualizada com sucesso", response.text)

    def test_06_deletar_atividade(self):
        response = requests.delete(f"{self.base_url}/atividades/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Atividade deletada com sucesso", response.text)

    def test_07_obter_atividade_inexistente(self):
        response = requests.get(f"{self.base_url}/atividades/999")
        self.assertEqual(response.status_code, 404)

    def test_08_atualizar_atividade_inexistente(self):
        dados = {"enunciado": "Qualquer coisa"}
        response = requests.put(f"{self.base_url}/atividades/999", json=dados)
        self.assertEqual(response.status_code, 404)

    def test_09_deletar_atividade_inexistente(self):
        response = requests.delete(f"{self.base_url}/atividades/999")
        self.assertEqual(response.status_code, 404)
        self.test_00_resetar_dados() # Resetar dados após os testes

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAtividadesAPI)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

if __name__ == "__main__":
    runTests()
