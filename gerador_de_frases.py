from faker import Faker
from random import choice, randint
fake = Faker()

class A1A_sentence_generator():
    def __init__(self):
        pass

    verbo_ser = {
        'eu' : 'sou',
        'você' : 'é',
        'ele' : 'é',
        'ela' : 'é',
        'nós' : 'somos',
        'vocês' : 'são',
        'eles' : 'são',
        'elas' : 'são'
    }

    verbo_ter = {
                'eu' : 'tenho',
                'você' : 'tem',
                'ele' : 'tem',
                'ela' : 'tem',
                'nós' : 'temos',
                'vocês' : 'tem',
                'eles' : 'tem',
                'elas' : 'tem'
            }

    verb_to_be = {
        'I' : 'am',
        'you': 'are',
        'he' : 'is',
        'she' : 'is',
        'we' : 'are',
        'they' : 'are'
    }
    pronouns = {
        'eu' : 'I',
        'você' : 'you',
        'ele' : 'he',
        'ela' : 'she',
        'nós' : 'we',
        'vocês' : 'you',
        'eles' : 'they',
        'elas' : 'they'
    }
    possessivos = {
            'meu nome' : 'é',
            'seu nome' : 'é',
            'o nome dele' : 'é',
            'o nome dela' : 'é',
            'nossos nomes' : 'são',
            'seus nomes' : 'são',
            'os nomes deles' : 'são'
        }

    possessives = {
            'meu nome' : 'my name',
            'seu nome' : 'your name',
            'o nome dele' : 'his name',
            'o nome dela' : 'her name',
            'nossos nomes' : 'our names',
            'seus nomes' : 'your names',
            'os nomes deles' : 'their names'
        }

    possessives_to_be = {
        'my name' : 'is',
        'your name' : 'is',
        'his name' : 'is',
        'her name' : 'is',
        'our names' : 'are',
        'your names' : 'are',
        'their names' : 'are'
     }

    def origem(self):
        sujeito = choice([key for key in self.verbo_ser.keys()])
        tipo = choice(['afirmativa', 'interrogativa', 'negativa'])
        sujeito_en = self.pronouns[sujeito]
        country = fake.country()
        if tipo == 'afirmativa':
            frase_en = f'{sujeito_en.capitalize()} {self.verb_to_be[sujeito_en]} from {country}'
            return tipo, f'{sujeito.capitalize()} {self.verbo_ser[sujeito]} do {country}', frase_en
    
        elif tipo == 'negativa':
            frase_en = f'{sujeito_en.capitalize()} {self.verb_to_be[sujeito_en]} not from {country}'
            return tipo, f'{sujeito.capitalize()} não {self.verbo_ser[sujeito]} do {country}', frase_en
    
        else:
            frase_en = f'{self.verb_to_be[sujeito_en].capitalize()} {sujeito_en} from {country}?'
            return tipo, f'{sujeito.capitalize()} {self.verbo_ser[sujeito]} do {country}?', frase_en

    def nome(self):
        sujeito = choice([key for key in self.possessivos.keys()])
        verb = self.possessivos[sujeito]
        tipo = choice(['afirmativa', 'interrogativa', 'negativa'])
        sujeito_en = self.possessives[sujeito]
        verb_en = self.possessives_to_be[sujeito_en]
        name_1 = fake.first_name()
        name_2 = fake.first_name()
        name_m = fake.first_name_male()
        name_f= fake.first_name_female()
        if tipo == 'afirmativa':
            if verb == 'são':
                frase_en = f'{sujeito_en.capitalize()} {verb_en} {name_1} and {name_2}'
                return tipo, f'{sujeito.capitalize()} {verb} {name_1} e {name_2}', frase_en
            else:
                if sujeito == 'o nome dele':
                    frase_en = f'{sujeito_en.capitalize()} {verb_en} {name_m}'
                    return tipo, f'{sujeito.capitalize()} {verb} {name_m}', frase_en
                elif sujeito == 'o nome dela':
                    frase_en = f'{sujeito_en.capitalize()} {verb_en} {name_f}'
                    return tipo, f'{sujeito.capitalize()} {verb} {name_f}', frase_en
                else:
                    frase_en = f'{sujeito_en.capitalize()} {verb_en} {name_1}'
                    return tipo, f'{sujeito.capitalize()} {verb} {name_1}', frase_en
    
        elif tipo == 'negativa':
            if verb == 'são':
                frase_en = f'{sujeito_en.capitalize()} {verb_en} not {name_1} and {name_2}'
                return tipo, f'{sujeito.capitalize()} não {verb} {name_1} e {name_2}', frase_en
            else:
                if sujeito == 'o nome dele':
                    frase_en = f'{sujeito_en.capitalize()} {verb_en} not {name_m}'
                    return tipo, f'{sujeito.capitalize()} não {verb} {name_m}', frase_en
                elif sujeito == 'o nome dela':
                    frase_en = f'{sujeito_en.capitalize()} {verb_en} not {name_f}'
                    return tipo, f'{sujeito.capitalize()} não {verb} {name_f}', frase_en
                else:
                    frase_en = f'{sujeito_en.capitalize()} {verb_en} not {name_1}'
                    return tipo, f'{sujeito.capitalize()} não {verb} {name_1}', frase_en

        else:
            if verb == 'são':
                frase_en = f'{verb_en.capitalize()} {sujeito_en} {name_1} and {name_2}?'
                return tipo, f'{sujeito.capitalize()} {verb} {name_1} e {name_2}?', frase_en
            else:
                if sujeito == 'o nome dele':
                    frase_en = f'{verb_en.capitalize()} {sujeito_en} {name_m}?'
                    return tipo, f'{sujeito.capitalize()} {verb} {name_m}?',frase_en
                elif sujeito == 'o nome dela':
                    frase_en = f'{verb_en.capitalize()} {sujeito_en} {name_f}?'
                    return tipo, f'{sujeito.capitalize()} {verb} {name_f}?', frase_en
                else:
                    frase_en = f'{verb_en.capitalize()} {sujeito_en} {name_1}?'
                    return tipo, f'{sujeito.capitalize()} {verb} {name_1}?', frase_en

    def idade(self):
        sujeito = choice([key for key in self.verbo_ter.keys()])
        verbo = self.verbo_ter[sujeito]
        idade = randint(1,110)
        tipo = choice(['afirmativa', 'interrogativa', 'negativa'])
        sujeito_en = self.pronouns[sujeito]
        verbo_en = self.verb_to_be[sujeito_en]
        if tipo == 'afirmativa':
            frase_en = f'{sujeito_en.capitalize()} {verbo_en} {idade} years old.'
            return tipo, f'{sujeito.capitalize()} {verbo} {idade} anos.', frase_en
    
        elif tipo == 'negativa':
            frase_en = f'{sujeito_en.capitalize()} {verbo_en} not {idade} years old.'
            return tipo, f'{sujeito.capitalize()} não {verbo} {idade} anos.', frase_en
    
        else:
            frase_en = f'{verbo_en.capitalize()} {sujeito_en} {idade} years old?'
            return tipo, f'{sujeito.capitalize()} {verbo} {idade} anos?', frase_en

    def gerar_frases(self):
        topics = {
            'origem' : self.origem,
            'nome' : self.nome,
            'idade' : self.idade
        }

        return topics[choice([key for key in topics.keys()])]()
if "__main__" == __name__:
    gerador = A1A_sentence_generator()
    for i in range(27):
        print(gerador.gerar_frases())
