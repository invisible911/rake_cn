from py4j.java_gateway import JavaGateway
from py4j.java_gateway import GatewayParameters

class tokenizer:
    def __init__(self,):
        ss = GatewayParameters(address = 'localhost',port = 15554)
        self.gateway = JavaGateway(gateway_parameters=ss) 
        self.tokenizer = self.gateway.entry_point
    def tokenize(self,sentenceText,):
        try:
            result = self.tokenizer.get_terms_words(sentenceText)
        except:
            return ""
        return result
    def tokenize_nature(self,sentenceText,):
        return self.tokenizer.get_terms_nature(sentenceText)