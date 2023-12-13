# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils.encoding import smart_str
import json, os, sys
from unicodedata import normalize
import re as regex

coding = sys.stdout.encoding

mips_functions = [
	{
		'name': 'add',
		'description': 'Adiciona X e Y e armazena o resultado no registrador Z',
		'example': 'add $s0, $s1, $s2',
		'code_equialency': 'z = x + y',
		'fname': 'add',
		'opcode': '000000',
		'funct': '100000',
		'format': 'R'
	}, {
		'name': 'addi',
		'description': 'Adiciona um inteiro ao registrador X e armazena o resultado no registrador Y',
		'example': 'addi $s0, $s1, 100',
		'code_equialency': 'y = x + 100',
		'fname': 'addi',
		'opcode': '001000',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'sub',
		'description': 'Subtrai Y de X e armazena o resultado no registrador Z',
		'example': 'sub $s0, $s1, $s2',
		'code_equialency': 'z = x - y',
		'fname': 'sub',
		'opcode': '000000',
		'funct': '100010',
		'format': 'R'
	}, {
		'name': 'mult',
		'description': 'Multiplica X e Y e armazena o resultado nos registradores "hi" e "lo"',
		'example': 'mult $s0, $s1',
		'code_equialency': 'lo = x * y; hi = (x * y) >> 32',
		'fname': 'mult',
		'opcode': '000000',
		'funct': '011000',
		'format': 'R'
	}, {
		'name': 'div',
		'description': 'Divide X por Y e armazena o resultado no registrador "lo" e o restante no registrador "hi"',
		'example': 'div $s0, $s1',
		'code_equialency': 'lo = x / y; hi = x % y',
		'fname': 'div',
		'opcode': '000000',
		'funct': '011010',
		'format': 'R'
	}, {
		'name': 'mfhi',
		'description': 'Move o valor do registrador "hi" para o registrador X',
		'example': 'mfhi $s0',
		'code_equialency': 'x = hi',
		'fname': 'mult',
		'opcode': '000000',
		'funct': '010000',
		'format': 'R'
	}, {
		'name': 'mflo',
		'description': 'Move o valor do registrador "lo" para o registrador X',
		'example': 'mflo $s0',
		'code_equialency': 'x = lo',
		'fname': 'div',
		'opcode': '000000',
		'funct': '010010',
		'format': 'R'
	}, {
		'name': 'and',
		'description': 'Define o registrador X como a operação AND bit a bit de Y e Z',
		'example': 'and $s0, $s1, $s2',
		'code_equialency': 'x = y & z',
		'fname': 'and',
		'opcode': '000000',
		'funct': '100100',
		'format': 'R'
	}, {
		'name': 'or',
		'description': 'Define o registrador X como a operação OR bit a bit de Y e Z',
		'example': 'or $s0, $s1, $s2',
		'code_equialency': 'x = y | z',
		'fname': 'or',
		'opcode': '000000',
		'funct': '100101',
		'format': 'R'
	}, {
		'name': 'xor',
		'description': 'Define o registrador X como a operação XOR bit a bit de Y e Z',
		'example': 'xor $s0, $s1, $s2',
		'code_equialency': 'x = y ^ z',
		'fname': 'xor',
		'opcode': '000000',
		'funct': '100110',
		'format': 'R'
	}, {
		'name': 'nor',
		'description': 'Define o registrador X como a operação NOR bit a bit de Y e Z',
		'example': 'nor $s0, $s1, $s2',
		'code_equialency': 'x = ~(y | z)',
		'fname': 'nor',
		'opcode': '000000',
		'funct': '100111',
		'format': 'R'
	}, {
		'name': 'sll',
		'description': 'Desloca o valor do registrador X para a esquerda por Y bits e armazena o resultado no registrador Z',
		'example': 'sll $s0, $s1, 2',
		'code_equialency': 'z = y << 2',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '000000',
		'format': 'R'
	}, {
		'name': 'srl',
		'description': 'Desloca o valor do registrador X para a direita por Y bits e armazena o resultado no registrador Z',
		'example': 'srl $s0, $s1, 2',
		'code_equialency': 'z = y >> 2',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '000010',
		'format': 'R'
	}, {
		'name': 'sra',
		'description': 'Desloca o valor do registrador X para a direita por Y bits e armazena o resultado no registrador Z',
		'example': 'sra $s0, $s1, 2',
		'code_equialency': 'z = y >> 2',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '000011',
		'format': 'R'
	}, {
		'name': 'sllv',
		'description': 'Desloca o valor do registrador X para a esquerda pelo valor do registrador Y e armazena o resultado no registrador Z',
		'example': 'sllv $s0, $s1, $s2',
		'code_equialency': 'z = y << x',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '000100',
		'format': 'R'
	}, {
		'name': 'srlv',
		'description': 'Desloca o valor do registrador X para a direita pelo valor do registrador Y e armazena o resultado no registrador Z',
		'example': 'srlv $s0, $s1, $s2',
		'code_equialency': 'z = y >> x',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '000110',
		'format': 'R'
	}, {
		'name': 'srav',
		'description': 'Desloca o valor do registrador X para a direita pelo valor do registrador Y e armazena o resultado no registrador Z',
		'example': 'srav $s0, $s1, $s2',
		'code_equialency': 'z = y >> x',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '000111',
		'format': 'R'
	}, {
		'name': 'slt',
		'description': 'Define o registrador X como 1 se Y for menor que Z, 0 caso contrário',
		'example': 'slt $s0, $s1, $s2',
		'code_equialency': 'if (y < z) x = 1; else x = 0',
		'fname': 'slt',
		'opcode': '000000',
		'funct': '101010',
		'format': 'R'
	}, {
		'name': 'slti',
		'description': 'Define o registrador X como 1 se Y for menor que o inteiro Z, 0 caso contrário',
		'example': 'slti $s0, $s1, 100',
		'code_equialency': 'if (y < 100) x = 1; else x = 0',
		'fname': 'slti',
		'opcode': '001010',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'sltu',
		'description': 'Define o registrador X como 1 se Y for menor que Z, 0 caso contrário',
		'example': 'sltu $s0, $s1, $s2',
		'code_equialency': 'if (y < z) x = 1; else x = 0',
		'fname': 'slt',
		'opcode': '000000',
		'funct': '101011',
		'format': 'R'
	}, {
		'name': 'sltiu',
		'description': 'Define o registrador X como 1 se Y for menor que o inteiro Z, 0 caso contrário',
		'example': 'sltiu $s0, $s1, 100',
		'code_equialency': 'if (y < 100) x = 1; else x = 0',
		'fname': 'slti',
		'opcode': '001011',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'j',
		'description': 'Salta para o endereço na etiqueta',
		'example': 'j label',
		'code_equialency': 'goto label',
		'fname': 'jump',
		'opcode': '000010',
		'funct': '',
		'format': 'J'
	}, {
		'name': 'jal',
		'description': 'Salta para o endereço na etiqueta e armazena o endereço de retorno no registrador 31',
		'example': 'jal label',
		'code_equialency': 'goto label; $ra = PC + 4',
		'fname': '', # TODO: add function name
		'opcode': '000011',
		'funct': '',
		'format': 'J'
	}, {
		'name': 'jr',
		'description': 'Salta para o endereço armazenado no registrador X',
		'example': 'jr $s0',
		'code_equialency': 'goto x',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '001000',
		'format': 'R'
	}, {
		'name': 'jalr',
		'description': 'Salta para o endereço armazenado no registrador X e armazena o endereço de retorno no registrador Y',
		'example': 'jalr $s0, $s1',
		'code_equialency': 'goto x; y = PC + 4',
		'fname': '', # TODO: add function name
		'opcode': '000000',
		'funct': '001001',
		'format': 'R'
	}, {
		'name': 'beq',
		'description': 'Salta para a etiqueta se X e Y forem iguais',
		'example': 'beq $s0, $s1, label',
		'code_equialency': 'if (x == y) goto label',
		'fname': 'beq',
		'opcode': '000100',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'bne',
		'description': 'Salta para a etiqueta se X e Y não forem iguais',
		'example': 'bne $s0, $s1, label',
		'code_equialency': 'if (x != y) goto label',
		'fname': 'bne',
		'opcode': '000101',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'syscall',
		'description': 'Chama o sistema operacional',
		'example': 'syscall',
		'code_equialency': 'chamar o sistema operacional',
		'fname': 'bne',
		'opcode': '000000',
		'funct': '001100',
		'format': 'R'
	}, {
		'name': 'lui',
		'description': 'Carrega o valor imediato nos 16 bits superiores do registrador X',
		'example': 'lui $s0, 100',
		'code_equialency': 'x = 100 << 16',
		'fname': '', # TODO: add function name
		'opcode': '001111',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'lb',
		'description': 'Carrega o byte no endereço X + Y no registrador Z',
		'example': 'lb $s0, 100($s1)',
		'code_equialency': 'z = memória[x + y]',
		'fname': '', # TODO: add function name
		'opcode': '100000',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'lbu',
		'description': 'Carrega o byte sem sinal no endereço X + Y no registrador Z',
		'example': 'lbu $s0, 100($s1)',
		'code_equialency': 'z = memória[x + y]',
		'fname': '', # TODO: add function name
		'opcode': '100100',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'lh',
		'description': 'Carrega a meia-palavra no endereço X + Y no registrador Z',
		'example': 'lh $s0, 100($s1)',
		'code_equialency': 'z = memória[x + y]',
		'fname': '', # TODO: add function name
		'opcode': '100001',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'lhu',
		'description': 'Carrega a meia-palavra sem sinal no endereço X + Y no registrador Z',
		'example': 'lhu $s0, 100($s1)',
		'code_equialency': 'z = memória[x + y]',
		'fname': '', # TODO: add function name
		'opcode': '100101',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'lw',
		'description': 'Carrega a palavra no endereço X + Y para o registrador Z',
		'example': 'lw $s0, 100($s1)',
		'code_equialency': 'z = memoria[x + y]',
		'fname': '', # TODO: add function name
		'opcode': '100011',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'sb',
		'description': 'Armazena o byte no registrador Z no endereço X + Y',
		'example': 'sb $s0, 100($s1)',
		'code_equialency': 'memoria[x + y] = z',
		'fname': '', # TODO: add function name
		'opcode': '101000',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'sh',
		'description': 'Armazena a meia palavra no registrador Z no endereço X + Y',
		'example': 'sh $s0, 100($s1)',
		'code_equialency': 'memoria[x + y] = z',
		'fname': '', # TODO: add function name
		'opcode': '101001',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'sw',
		'description': 'Armazena a palavra no registrador Z no endereço X + Y',
		'example': 'sw $s0, 100($s1)',
		'code_equialency': 'memoria[x + y] = z',
		'fname': '', # TODO: add function name
		'opcode': '101011',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'll',
		'description': 'Carrega a palavra no endereço X + Y para o registrador Z e define o bit de bloqueio',
		'example': 'll $s0, 100($s1)',
		'code_equialency': 'z = memoria[x + y]; lock = 1',
		'fname': '', # TODO: add function name
		'opcode': '110000',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'sc',
		'description': 'Armazena a palavra no registrador Z no endereço X + Y e limpa o bit de bloqueio',
		'example': 'sc $s0, 100($s1)',
		'code_equialency': 'memoria[x + y] = z; lock = 0',
		'fname': '', # TODO: add function name
		'opcode': '111000',
		'funct': '',
		'format': 'I'
	}, {
		'name': 'bge',
		'description': 'Desvia para o rótulo se X for maior ou igual a Y',
		'example': 'bge $s0, $s1, label',
		'code_equialency': 'se (x >= y) vá para o rótulo',
		'fname': 'bge',
		'opcode': '000001',
		'funct': '101000',
		'format': 'I'
	}, {
		'name': 'bgt',
		'description': 'Desvia para o rótulo se X for maior que Y',
		'example': 'bgt $s0, $s1, label',
		'code_equialency': 'se (x > y) vá para o rótulo',
		'fname': 'bgt',
		'opcode': '000111',
		'funct': '000000',
		'format': 'I'
	}, {
		'name': 'ble',
		'description': 'Desvia para o rótulo se X for menor ou igual a Y',
		'example': 'ble $s0, $s1, label',
		'code_equialency': 'se (x <= y) vá para o rótulo',
		'fname': 'ble',
		'opcode': '000110',
		'funct': '000000',
		'format': 'I'
	}, {
		'name': 'blt',
		'description': 'Desvia para o rótulo se X for menor que Y',
		'example': 'blt $s0, $s1, label',
		'code_equialency': 'se (x < y) vá para o rótulo',
		'fname': 'blt',
		'opcode': '000001',
		'funct': '000000',
		'format': 'I'
	}, {
		'name': 'la',
		'description': 'Carrega o endereço do rótulo para o registrador X',
		'example': 'la $s0, label',
		'code_equialency': 'x = rótulo',
		'fname': '', # TODO: add function name
		'opcode': '',
		'funct': '',
		'format': ''
	}, {
		'name': 'li',
		'description': 'Carrega o inteiro para o registrador X',
		'example': 'li $s0, 100',
		'code_equialency': 'x = 100',
		'fname': 'bne',
		'opcode': '',
		'funct': '',
		'format': ''
	}, {
		'name': 'move',
		'description': 'Move o valor do registrador Y para o registrador X',
		'example': 'move $s0, $s1',
		'code_equialency': 'x = y',
		'fname': 'bne',
		'opcode': '',
		'funct': '',
		'format': ''
	}, {
		'name': 'nop',
		'description': 'Não faz nada',
		'example': 'nop',
		'code_equialency': 'não faça nada',
		'fname': '', # TODO: add function name
		'opcode': '',
		'funct': '',
		'format': ''
	}
]

def __get_function_by_name(name):
	global mips_functions
	for func in mips_functions:
		if func['name'] == name:
			return func
	return {
		'name': ''
	}

def main(req):
	global mips_functions
	toSend = {
		'functions': mips_functions
	}
	template = loader.get_template('main.html')
	return HttpResponse(template.render(toSend, req))

def func_view(req, func_name = ""):
	toSend = __get_function_by_name(func_name)
	examples = {
		'code': "",
		'assembly': ""
	}
	if toSend['fname'] != '':
		# reading all lines from the files "codes/c/<function_name>.c" and "codes/asm/<function_name>.asm"
		# and saving them in the variables "code" and "assembly", respectively
		try:
			with open(os.path.join(os.path.dirname(__file__), "codes/c/" + toSend['fname'] + ".c"), "r") as f:
				examples['code'] = f.read()
		except:
			examples['code'] = ""
		try:
			with open(os.path.join(os.path.dirname(__file__), "codes/asm/" + toSend['fname'] + ".asm"), "r") as f:
				examples['assembly'] = f.read()
		except:
			examples['assembly'] = ""
	toSend['examples'] = {
		'code': examples['code'],
		'lang': "c",
		'assembly': examples['assembly']
	}

	template = loader.get_template('funcao.html')
	return HttpResponse(template.render(toSend, req))

def exemples(req):
	# scaneando o diretorio "premade_exemple" procurando por todas as pastas que tenham um arquivo "code.asm" e um "info.json"
	# e salvando as informações de cada exemplo na variavel "exemple"
	exemple = []
	for root, dirs, files in os.walk(os.path.join(os.path.dirname(__file__), "premade_exemple")):
		if "code.asm" in files and "data.json" in files:
			with open(os.path.join(root, "data.json"), "r", encoding="utf-8") as f:
				exemple.append(json.load(f))
				# exemple[-1]['Name'] = smart_str(exemple[-1]['Name'])

			with open(os.path.join(root, "code.asm"), "r") as f:
				exemple[-1]['Code'] = f.read()

	# substituindo **{text}** por <b>{text}</b>, *{text}* por <i>{text}</i> e `{text}` por <code>{text}</code>
	# usando regex para substituir todas as ocorrências
	for i in range(len(exemple)):
		for j in ['Name', 'Desc']:
			# exemple[i][j] = unicode(exemple[i][j], errors='replace')
			exemple[i][j] = regex.sub(r"\*\*([^\*]+)\*\*", r"<b>\1</b>", exemple[i][j])
			exemple[i][j] = regex.sub(r"\*([^\*]+)\*", r"<i>\1</i>", exemple[i][j])
			exemple[i][j] = regex.sub(r"`([^\`]+)`", r"<code>\1</code>", exemple[i][j])
			print(exemple[i][j])

	toSend = {
		'exemples': exemple
	}
	template = loader.get_template('premade_exemples.html')
	return HttpResponse(template.render(toSend, req))
