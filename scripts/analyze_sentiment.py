import os
import requests
import uuid
import json
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

class AzureTextAnalyzer:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_ENDPOINT", "").rstrip('/')
        self.key = os.getenv("AZURE_KEY", "")
        self.validate_credentials()
        
    def validate_credentials(self):
        if not self.endpoint or not self.key:
            raise ValueError("AZURE_ENDPOINT e AZURE_KEY devem ser definidos no .env")
        
        if "cognitiveservices.azure.com" not in self.endpoint:
            raise ValueError("Endpoint do Azure deve conter 'cognitiveservices.azure.com'")

    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Analisa o sentimento do texto usando Azure Language Service"""
        url = f"{self.endpoint}/language/analyze-text?api-version=2023-11-15"  # Versão mais recente
        
        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4())
        }

        body = {
            "kind": "SentimentAnalysis",
            "parameters": {"modelVersion": "latest"},
            "analysisInput": {
                "documents": [{
                    "id": "1",
                    "language": "pt",
                    "text": text
                }]
            }
        }

        try:
            response = requests.post(url, headers=headers, json=body, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error_msg = f"Erro na requisição: {str(e)}"
            if hasattr(e, 'response') and e.response:
                error_msg += f"\nResposta: {e.response.text}"
            raise ConnectionError(error_msg) from e

    @staticmethod
    def save_results(data: Dict[str, Any], filename: str) -> None:
        """Salva os resultados em JSON"""
        os.makedirs("results", exist_ok=True)
        with open(f"results/{filename}", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def print_summary(result_json: Dict[str, Any]) -> None:
        """Exibe um resumo formatado da análise"""
        try:
            doc = result_json["results"]["documents"][0]
            print("\n🔎 Análise de Sentimento")
            print("-----------------------")
            print(f"Sentimento geral: {doc['sentiment'].upper()}")
            print(f"👍 Positivo: {doc['confidenceScores']['positive']:.2%}")
            print(f"😐 Neutro:   {doc['confidenceScores']['neutral']:.2%}")
            print(f"👎 Negativo: {doc['confidenceScores']['negative']:.2%}\n")
        except (KeyError, IndexError) as e:
            print("⚠️ Não foi possível extrair o resumo da análise.")
            print("Resposta completa recebida:")
            print(json.dumps(result_json, ensure_ascii=False, indent=2))

    def test_connection(self) -> bool:
        """Testa a conexão com o serviço Azure"""
        test_url = f"{self.endpoint}/language/analyze-text/jobs"
        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(test_url, headers=headers, timeout=5)
            return response.status_code in (200, 401, 403)  # 401/403 indicam que o endpoint existe
        except requests.exceptions.RequestException as e:
            print(f"🔴 Falha na conexão: {str(e)}")
            return False


# Exemplo de uso:
if __name__ == "__main__":
    try:
        analyzer = AzureTextAnalyzer()
        
        print("Testando conexão com Azure...")
        if analyzer.test_connection():
            print("✅ Conexão estabelecida com sucesso!")
            
            sample_text = "Azure Language Service é incrível para análise de sentimentos!"
            print(f"\nAnalisando texto: '{sample_text}'")
            
            result = analyzer.analyze_text(sample_text)
            analyzer.print_summary(result)
            analyzer.save_results(result, "exemplo_analise.json")
        else:
            print("❌ Falha ao conectar ao Azure. Verifique suas credenciais.")
    except Exception as e:
        print(f"❌ Erro crítico: {str(e)}")