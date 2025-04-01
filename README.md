# nubank-cut-notas-negociacao
### Projeto livre para cortar de notas de negociação nubank, facilitando imposto de renda.

Para rodar, primeiro retire suas notas clicando na sua imagem no nubank e clicando em documentos -> documentos para imposto ou similar.

Então, faça o pedido de todas suas notas de negociação no periodo.

Após criar uma pasta target (./build.sh create-target), guarde suas notas no diretório target. Todos devem ser pdf

```
(exemplo:)
├── build.sh
├── main.py
├── README.md
├── requirements.txt
└── target
    ├── 36766.pdf
    ├── 36884.pdf
    ├── 44642.pdf
    ├── 46551.pdf
    ├── 46676.pdf
    ├── 48262.pdf
    ├── 52722.pdf
    ├── 53692.pdf
    ├── 54514.pdf
    ├── 55767.pdf
    ├── 58434.pdf
    ├── 59781.pdf
    └── 60405.pdf
``'''``

após isso, basta executar o comando da venv (./build.sh venv) para criar uma venv e baixar suas dependências e após isso, executar o comando run (./build.sh run), que será responsável por executar o comando main.py passando como argumento o diretório target.

Você pode mudar o Mercado (fixado BOVESPA por necessidade pessoal) ou o retorno como quiser. O corte do nome real completo do ativo também é realizado por pura necessidade pessoal.

Retorno (exemplo de valores não reais):
item valor
BRKM5F 29312.60
C1TA34 46213.68
GGBR4F 4211.10

