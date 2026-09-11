from faker import Faker
from random import choice, randint
import json
fake = Faker()

class A1A_sentence_generator():
    def __init__(self):
        pass
    
    with open("conjugation.json", "r", encoding="utf-8") as f:
        conjugation = json.load(f)
    
    with open("countries.json", "r", encoding="utf-8") as f:
        countries = json.load(f)

    def origem(self):
        tipo = choice(['afirmativa', 'interrogativa', 'negativa'])
        country = choice([key for key in self.countries.keys()])

        sujeito = choice([key for key in self.conjugation['ser'].keys()])
        verb = self.conjugation['ser'][sujeito]
        sujeito_en = self.conjugation['pronouns'][sujeito]
        verb_en = self.conjugation['to_be'][sujeito_en]
        country_en = self.countries[country]['english']
        
        if tipo == 'afirmativa':
            frase_en = f'{sujeito_en.capitalize()} {verb_en} from {country_en}'
            return tipo, f'{sujeito.capitalize()} {verb} {self.countries[country]['preposition']} {country}', frase_en
    
        elif tipo == 'negativa':
            frase_en = f'{sujeito_en.capitalize()} {verb_en} not from {country_en}'
            return tipo, f'{sujeito.capitalize()} não {verb} {self.countries[country]['preposition']} {country}', frase_en
    
        else:
            frase_en = f'{verb_en.capitalize()} {sujeito_en} from {country_en}?'
            return tipo, f'{sujeito.capitalize()} {verb} {self.countries[country]['preposition']} {country}?', frase_en

    def nome(self):
        tipo = choice(['afirmativa', 'interrogativa', 'negativa'])
        name_1 = fake.first_name()
        name_2 = fake.first_name()
        name_m = fake.first_name_male()
        name_f= fake.first_name_female()

        sujeito = choice([key for key in self.conjugation['possessivos'].keys()])
        verb = self.conjugation['possessivos'][sujeito]
        sujeito_en = self.conjugation['possessives'][sujeito]
        verb_en = self.conjugation['possessives_to_be'][sujeito_en]
        
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
        tipo = choice(['afirmativa', 'interrogativa', 'negativa'])
        idade = randint(2,110)

        sujeito = choice([key for key in self.conjugation['ter'].keys()])
        verbo = self.conjugation['ter'][sujeito]
        sujeito_en = self.conjugation['pronouns'][sujeito]
        verbo_en = self.conjugation['to_be'][sujeito_en]


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
