import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime
import plotly.graph_objects as go
import numpy as np
from streamlit_folium import st_folium
import streamlit as st



st.set_page_config(
    page_title="Relatório Técnico Cálculo de Carga Térmica",
    page_icon="📄",
    layout="wide"
)

# Injetando CSS para customizar os botões
st.markdown("""
    <style>
    .button-style {
        background-color: #FF4B4B;
        color: white;
        border: none;
        width: 100%;
        height: 50px;
        font-size: 16px;
        text-align: center;
        line-height: 50px;
        margin-bottom: 10px;
        border-radius: 10px;
        cursor: pointer;
    }

    .button-style:hover {
        background-color: #ff3333;
    }

    .expander-style {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Variável de controle de navegação
pagina_selecionada = "Sobre"  # Exibe a página "Sobre" por padrão

# Estilo da Sidebar e Navegação
st.sidebar.title("Secões disponíveis")

# Seção 1: Caracterização, Diagnósticos e Recomendações
with st.sidebar.expander("Seção 1"):
    if st.button("Local Analisado", key="pagina_inicial", use_container_width=True):
        pagina_selecionada = "Sobre"
    
    if st.button("Caracterização Interna da Edificação", key="caracterizacao_imovel", use_container_width=True):
        pagina_selecionada = "Caracterização Interna da Edificação"
    
    if st.button("Caracterização de João Pessoa", key="caracterizacao_jp", use_container_width=True):
        pagina_selecionada = "Caracterização de João Pessoa"
    
    if st.button("Diagnóstico de Conforto", key="diagnostico_conforto", use_container_width=True):
        pagina_selecionada = "Diagnóstico de Conforto"
    
    if st.button("Carta Solar", key="carta_solar", use_container_width=True):
        pagina_selecionada = "Carta Solar"

    if st.button("Rosa dos Ventos", key="rosa_dos_ventos", use_container_width=True):
        pagina_selecionada = "Rosa dos Ventos"

# Seção 2: Novas Análises
with st.sidebar.expander("Seção 2"):

    if st.button("Carga Térmica Total", key="carga_termica", use_container_width=True):
        pagina_selecionada = "Carga Térmica Total"

    if st.button("Sistema Proposto", key="sistema_proposto", use_container_width=True):
        pagina_selecionada = "Sistema Proposto"

    if st.button("Responsabilidade Técnica", key="responsabilidade_tecnica", use_container_width=True):
        pagina_selecionada = "Responsabilidade Técnica"





# Exibição da página selecionada
if pagina_selecionada == "Sobre":
    st.title("Relatório Técnico : Cálculo de Carga Térmica")
    st.subheader("Paróquia São Francisco de Assis - João Pessoa, PB")

    st.write("""
    Este relatório técnico foi ofertado para Paróquia São Francisco de Assis está situada na Rua Joaquim Borba Filho, nº
413, no bairro Jardim São Paulo, município de João Pessoa, estado da Paraíba, Brasil.
    """)


    # Usando um card visual para simplificar o escopo
    col1, col2 = st.columns([1, 3])  # Ajusta a proporção entre texto e imagem

    with col1:
        
         st.image("img/igreja.jpg", caption="Paróquia São Francisco de Assis", use_container_width=True)

    with col2:
       
        st.markdown("""
        <div style="background-color:#f0f0f5;padding:20px;border-radius:10px">
        <h4 style="color:#333;text-align:center;">Escopo do Relatório</h4>
        <p style="text-align:justify; color:#555;">
        Este relatório apresenta uma análise detalhada das condições ambientais da Paróquia São Francisco de Assis, 
        com foco no desenvolvimento de um sistema de climatização eficiente e adequado às características do espaço. 
        A primeira etapa do estudo consistiu na caracterização do imóvel, considerando sua localização geográfica, 
        orientação solar, dimensões, materiais construtivos e padrão de ocupação. Paralelamente, foram elaboradas a
        carta solar e a carta bioclimática da região, permitindo uma avaliação precisa das variáveis climáticas que 
        influenciam diretamente o conforto térmico no interior da igreja. 
        </p>
        </div>
        """, unsafe_allow_html=True)
        # Mapa abaixo das colunas
       
    latitude = -7.151556
    longitude = -34.848750

    # Cria o mapa
    m = folium.Map(location=[latitude, longitude], zoom_start=17, width='100%', height='600')
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=6,
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(m)

    # Título da seção
    st.markdown("### Localização da Paróquia São Francisco de Assis")

    # Exibe o mapa com st_folium
    st_folium(m, width=1800, height=300)  # você pode ajustar o tamanho se quiser

  

elif pagina_selecionada == "Caracterização Interna da Edificação":

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Planta Baixa da Paróquia")
        st.image("img/planta.png", caption="Planta Baixa",width=400) 

    with col2:
    
          st.subheader("Características Físicas")
          st.image("img/janela_porta.png", caption="Portas e janela da Igreja",width=400) 
          st.image("img/salao.png", caption="Salão paroquial",width=400) 
    
    # Tabela 1 – Dimensões gerais da Igreja
    st.subheader("Dimensões gerais da Igreja")
    dados_dimensoes = {
        "Medida": ["Comprimento", "Largura", "Altura do pé-direito", "Espessura das paredes", "Área"],
        "Valor": ["57,20 m", "24,20 m", "4,00 m", "0,22 m", "1.384,24 m²"]
    }
    df_dimensoes = pd.DataFrame(dados_dimensoes)
    st.table(df_dimensoes)
    st.caption("Fonte: Elaboração própria (2025)")

    st.markdown("---")  # Linha divisória

    # Tabela 2 – Dimensões das aberturas e da edificação
    st.subheader(" Dimensões das aberturas e da edificação")
    dados_aberturas = {
        "Componente": ["Janelas", "Aberturas de cimento", "Porta de entrada principal", "Porta da sacristia", "Portas laterais"],
        "Quantidade": [8, 11, 1, 1, 4],
        "Largura (m)": [1.42, 1.42, 2.70, 2.70, 1.55],
        "Altura (m)": [1.96, 1.96, 3.00, 3.00, 2.17]
    }
    df_aberturas = pd.DataFrame(dados_aberturas)
    st.table(df_aberturas)
    st.caption("Fonte: Elaboração própria (2025)")

    

    st.markdown("É importante afirmar que as aberturas de cimento serão consideradas fechadas para esse relatório.")
    st.markdown("---")  # Espaço visual

    # Tabela 3 – Materiais construtivos e acabamento
    st.subheader("Materiais construtivos e acabamento")
    dados_materiais = {
        "Elemento": ["Paredes", "Telhado", "Fachada", "Piso", "Janelas"],
        "Material / Acabamento": [
            "Alvenaria revestida com cimento",
            "Telha de fibrocimento (brasilit)",
            "Cimento aparente",
            "Porcelanato fosco",
            "Vidro com película"
        ]
    }
    df_materiais = pd.DataFrame(dados_materiais)
    st.table(df_materiais)
    st.caption("Fonte: Elaboração própria (2025)")

    st.subheader("Equipamentos")

    dados_eletronicos = {
        "Equipamento": [
            "Lâmpadas",
            "Refletores",
            "Ventiladores de parede",
            "Ventiladores de coluna",
            "Caixas de som",
            "Lâmpada vermelha",
            "Câmera",
            "Microfones",
            "Bebedouro",
            "Mesa de som",
            "Teclado"
        ],
        "Quant.": [3, 14, 10, 3, 4, 1, 1, 7, 1, 1, 1],
        "Pot. unitária (W)": [60, 25, 200, 140, 1000, 6, 7, 4, 97, 9, 14],
        "Pot. total (W)": [180, 350, 2000, 420, 4000, 6, 7, 28, 97, 9, 14]
    }

    df_eletronicos = pd.DataFrame(dados_eletronicos)

    # Adicionando a linha de total
    total_pot = df_eletronicos["Pot. total (W)"].sum()
    df_eletronicos.loc["Total"] = ["–", "–", "–", total_pot]

   

    col1, col2 = st.columns([2, 1])  # Pode ajustar proporções conforme quiser

    with col1:
        st.table(df_eletronicos)
        st.caption("Fonte: Elaboração própria (2025)")

    with col2:
        st.image("img/equipamentos.png", caption="Equipamentos", width=400)

    
elif pagina_selecionada == "Responsabilidade Técnica":
    st.subheader("Equipe Técnica")
    st.markdown("""
            <div style="text-align: justify;">
                Este relatório técnico foi desenvolvido no âmbito da disciplina Condicionamento de Ar, 
                Ventilação e Refrigeração, ministrada pela Profª Drª Taynara Lago, pelas alunas do 
                curso de Engenharia de Energias Renováveis: Gabriela Tourinho, Júlia Ribeiro e Andressa Kátia.
            """, unsafe_allow_html=True)
    

    # Criação de três colunas para exibir as fotos lado a lado
    col1, col2, col3, col4 = st.columns(4)

     # Coluna 1 - Eng. Julia Alves
    with col1:
        st.image("img/tay-photoaidcom-cropped.png", caption="Profª Drª Taynara Lago", use_container_width=True)

    # Coluna 1 - Eng. Julia Alves
    with col2:
        st.image("img/gabi.png", caption="Gabriela Tourinho", use_container_width=True)

    # Coluna 2 - Eng. Julia Ribeiro
    with col3:
        st.image("img/ju2.jpg", caption="Julia Ribeiro", use_container_width=True)

    # Coluna 3 - Eng. Andressa Kátia
    with col4:
        st.image("img/andressa.jpg", caption="Andressa Kátia", use_container_width=True)




elif pagina_selecionada == "Caracterização de João Pessoa":
    st.header("João Pessoa")  
    st.markdown("""
            <div style="text-align: justify;">
                 A cidade de João Pessoa, capital do Estado da Paraíba, situada 
                a aproximadamente a 7°S de latitude e 34°W de longitude, possui 
                um clima tropical úmido, caracterizado por temperaturas elevadas 
                e pouca variação ao longo do ano. As médias anuais variam em torno 
                de 25°C a 28°C, com máximas que podem atingir 31°C e mínimas raramente
                abaixo de 22°C, de acordo com o INMET como mostrado a seguir.
            """, unsafe_allow_html=True)
    
    df = pd.read_excel("data/normais.xlsx")

    fig = go.Figure()

    # Adicionando as linhas e os marcadores
    fig.add_trace(go.Scatter(x=df["Mês"], y=df["Temp. Média (°C)"],
                            mode='lines+markers',
                            name='Temp. Média (°C)'))

    fig.add_trace(go.Scatter(x=df["Mês"], y=df["Temp. Miníma Média (°C)"],
                            mode='lines+markers',
                            name='Temp. Miníma Média (°C)'))

    fig.add_trace(go.Scatter(x=df["Mês"], y=df["Temp. Máxima Média (°C)"],
                            mode='lines+markers',
                            name='Temp. Máxima Média (°C)'))

    # Nomeando os eixos e adicionando o título
    fig.update_layout(title=""" Normais climatológicas (1991- 2020) da temperatura do ar para a estação João Pessoa - PB.""",
                    xaxis_title="Mês do Ano",
                    yaxis_title="Temperatura (°C)",
                    legend_title="Tipo de Temperatura",
                    width=800,   
                    height=400)


    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig)
    st.markdown("""
            <div style="text-align: justify;">
                A amplitude térmica diária normalmente não ultrapassa os 10°C, 
                segundo revelam as séries históricas. Isso se deve, basicamente, 
                aos fatores de baixa altitude e proximidade com o oceano Atlântico.
                De acordo com as Normais Climatológicas do INMET, para os anos de 1991 a 2020, 
                o número de horas de brilho solar (insolação) é maior nos meses de outubro a 
                janeiro. O total de horas de insolação anual média é de 2.673 horas.
                Nesse sentido, por terem dias mais curtos devido à posição do Sol, os meses de inverno, 
                além da alta nebulosidade e precipitação, exibem menos horas de insolação do que os meses de verão. 
                A máxima insolação mensal é de 266,1 horas em outubro, enquanto a mínima insolação mensal é 
                de 165 horas em junho. 
            """, unsafe_allow_html=True)
    
    figs = go.Figure()
    #Grafico insolação
    figs.add_trace(go.Bar(
        x=df['Mês'],
        y=df['Insolação Total (h)'],
        marker_color='orange',
        name='Insolação Mensal'
    ))

    figs.update_layout(
        title='Normais climatológicas (1991-2020) de insolação total para a estação João Pessoa- PB',
        xaxis_title='Mês',
        yaxis_title='Insolação (horas)',
        width=800,
        height=400
    )
    st.plotly_chart(figs)

    st.markdown("""
            <div style="text-align: justify;">
                Com relação a precipitação acumulada total nesse mesmo período, 
                as normais climatológicas de precipitação  revelam nitidamente 
                os períodos seco (setembro a fevereiro) e chuvoso (março a agosto) em João Pessoa. 
                O mínimo valor total mensal ocorre em novembro (21,10 mm), enquanto o máximo mensal 
                se dá em junho (368,70 mm). Assim, o total anual de precipitação é de 1837,40 mm.
            """, unsafe_allow_html=True)
    
    # Gráfico Precipitação
    pre = go.Figure()
    pre.add_trace(go.Bar(
        x=df['Mês'],
        y=df['Precipitação (mm)'],
        marker_color='blue',
        name='Precipitação Mensal'
    ))
    pre.update_layout(
        title='Precipitação Acumulada Mensal (1991-2020) - João Pessoa, PB',
        xaxis_title='Mês',
        yaxis_title='Precipitação (mm)',
        width=800,
        height=400
    )
    st.plotly_chart(pre)

    
    st.markdown("""
            <div style="text-align: justify;">
                Acerca da umidade relativa do ar, seus níveis variam de forma inversa
                à temperatura do ar e são influenciados pelos processos de aquecimento 
                ou resfriamento, pelo transporte horizontal de vapor d'água e pela precipitação. 
                Durante períodos de precipitação, ela pode alcançar 100% por um certo período. 
                Sendo assim, as normais climatológicas de umidade relativa do ar para a estação 
                de João Pessoa (PB)  indicam uma variação sazonal sutil, com o valor
                 mínimo de 72,4% registrado em outubro e o valor máximo de 82,1% em junho. 
                A média anual da umidade relativa é de 76,2%. Vale ressaltar também os 
                ventos provenientes do oceano transportando umidade para as regiões próximas 
                à costa durante a maior parte do ano. 

            """, unsafe_allow_html=True)
    
    umi = go.Figure()

    umi.add_trace(go.Bar(
        x=df['Mês'],
        y=df['Umidade Relativa (%)'],
        marker_color='green',
        name='Umidade Mensal'
    ))
    umi.update_layout(
        title='Umidade Mensal (1991-2020) - João Pessoa, PB',
        xaxis_title='Mês',
        yaxis_title= 'Umidade Relativa (%)',
        width=800,
        height=400
    )
    st.plotly_chart(umi)



    
elif pagina_selecionada == "Diagnóstico de Conforto":
    st.subheader("Zonas Bioclimáticas")
 
    st.markdown("""<div style="text-align: justify;">As zonas bioclimáticas são regiões geográficas classificadas de acordo com as características 
                climáticas predominantes, como temperatura, umidade, radiação solar e velocidade do vento. 
                Essa classificação permite a análise do comportamento climático de uma área específica, 
                auxiliando no desenvolvimento de estratégias de construção e design que otimizam o conforto térmico, 
                a eficiência energética e a sustentabilidade de edificações.
                Utilizamos o método das retas normais para traçar as zonas bioclimáticas
                de João Pessoa. Logo, as Retas Normais delimitadas para a cidade 
                João Pessoa na carta bioclimática estão expostas na figura abaixo.""", unsafe_allow_html=True)

    st.image("img/carta.png", use_container_width=True)

    html_table = """
    <div style="display: flex; justify-content: center; align-items: center; padding: 20px;">
    <table style="width:50%; border: 1px solid black; border-collapse: collapse;">
        <tr>
            <td style="border: 1px solid black;" rowspan="7"><strong>Desconforto</strong></td>
            <td style="border: 1px solid black;" colspan="2"><strong>Calor</strong></td>
        </tr>
        <tr>
            <td style="border: 1px solid black;">Ventilação</td>
            <td style="border: 1px solid black;">56,68</td>
        </tr>
        <tr>
            <td style="border: 1px solid black;">Ar Condicionado</td>
            <td style="border: 1px solid black;">3,75</td>
        </tr>
        <tr>
            <td style="border: 1px solid black;">Ventilação e Inércia Térmica para Resfriamento</td>
            <td style="border: 1px solid black;">1,76</td>
        </tr>
        <tr>
            <td style="border: 1px solid black;">Ventilação e Inércia Térmica para Resfriamento e Resfriamento Evaporativo</td>
            <td style="border: 1px solid black;">9,29</td>
        </tr>
        <tr>
            <td style="border: 1px solid black;" colspan="2"><strong>Frio</strong></td>
        </tr>
        <tr>
            <td style="border: 1px solid black;">Aquecimento Solar com Inércia Térmica</td>
            <td style="border: 1px solid black;">0,98</td>
        </tr>
        <tr>
            <td style="border: 1px solid black;" colspan="2"><strong>Total de Desconforto:</strong> 72,47</td>
        </tr>
        <tr>
            <td style="border: 1px solid black;" colspan="2"><strong>Conforto:</strong> 27,53</td>
        </tr>
    </table>
</div>
"""


    # Exibir a tabela HTML no Streamlit
    st.subheader("Diagnóstico de Conforto e Desconforto Térmico")
    st.markdown(html_table, unsafe_allow_html=True)

    # Subtítulo
    st.subheader('Resumo das condições de conforto térmico ao longo do ano')

    # Texto formatado com tópicos
    st.write("""
    - **Conforto térmico natural** está presente em **27,53% do tempo** ao longo do ano, sem necessidade de intervenções.
    - **72,47% do tempo** há desconforto térmico devido ao calor:
    - **Ventilação natural** é eficaz em **56,68% das situações**.
    - **Ar condicionado** é necessário em **3,75% dos casos**.
    - **Alta inércia térmica e resfriamento evaporativo** são essenciais em **9,29% das situações** de calor extremo.
    - **Desconforto por frio** é raro, ocorrendo apenas em **0,98% do tempo**:
    """)
    
  


elif pagina_selecionada == "Carta Solar":
    st.header('Carta Solar')


    st.markdown("""
        <div style="text-align: justify;">
        A carta solar é uma ferramenta essencial no planejamento arquitetônico,
        especialmente em projetos que visam maximizar o conforto e a eficiência energética, 
        como no caso de igrejas. A conversão solar transforma a trajetória solar em uma representação
        2D para fácil leitura.

            """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.image("img/cs1.jpg", width=300)
        
    with col2:
        
        st.subheader("O uso da carta solar permite:")
        st.write("""
        - Análisar a trajetória do sol ao longo do ano;
        - Identificar as fachadas mais expostas ao sol e das que permanecem sombreadas em diferentes horários e estações;
        - Definir as melhores estratégias para garantir condições ideais de iluminação;
        """)
        
    st.subheader("Análise de Horas de Sol")
    
    st.markdown("""
            <div style="text-align: justify;">
            O quadro a seguir apresenta as quantidades de horas de sol nos solstícios,
            que marcam o início do verão e do inverno. Nos solstícios, 
            o sol atinge sua maior declinação em relação à Linha do Equador. 
            Durante o solstício de verão, o hemisfério sul recebe o maior número de horas de sol,
            já que o sol se aproxima do Trópico de Capricórnio. No solstício de inverno, 
            o sol se aproxima do Trópico de Câncer, reduzindo as horas de sol no hemisfério sul. 
            Nos equinócios, o sol incide diretamente sobre o Equador, 
            distribuindo a mesma quantidade de radiação para os dois hemisférios.

            """, unsafe_allow_html=True)
    
    data = {
    "Fenômenos Astronômicos": ["Solstício de Verão", "Equinócios", "Solstício de Inverno"],
    "Datas": ["22/Dez", "21/Mar e 23/Set", "22/Jun"],
    "Horas de Sol": ["12h26min", "12h00min", "11h33min"]
}

    df = pd.DataFrame(data)

    # Exibindo a tabela no Streamlit
    st.table(df)
    
    

elif pagina_selecionada == "Rosa dos Ventos":
    st.subheader('Rosa dos Ventos')

    st.markdown("""
            <div style="text-align: justify;">
            A análise da rosa dos ventos é essencial para o projeto de refrigeração natural
            da paróquia, pois permite tomar decisões mais eficientes em relação à orientação das
            aberturas, ao aproveitamento dos ventos predominantes e ao uso de estratégias passiva de conforto térmico. 
            

            """, unsafe_allow_html=True)
    

    col1, col2 = st.columns(2)
   
    with col1:
        st.image("img/rosa.png", width=300)
        
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Análise dos Ventos em João Pessoa")

        st.markdown("""
        - **Ventos predominantes**: direção **norte**, com velocidades entre **4 e 6 m/s**, mais intensos na **primavera**.
        - **Outras direções favoráveis**: **sudeste e sul**, especialmente no **inverno, outono e primavera**.
        - **Direções desfavoráveis**: **oeste, noroeste e sudoeste**, com ventos fracos e pouco frequentes.
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("🏛️ Avaliação da Orientação da Paróquia")

    st.markdown("""
    - **Fachada principal voltada para sudoeste**: pouco favorecida pelos ventos predominantes.
    - **Aberturas voltadas para o leste**: bem posicionadas para **captar os ventos predominantes**, favorecendo a **ventilação natural** nos períodos mais quentes.
    - **Aberturas a oeste**: mesmo com pouco vento, são importantes para **permitir a saída do ar** e garantir **ventilação cruzada**.
    """)

    st.subheader("☀️ Considerações Térmicas")

    st.markdown("""
    - **Fachadas leste e oeste** recebem **radiação solar direta**:
        - Leste: exposição ao **sol da manhã**.
        - Oeste: exposição ao **sol da tarde**.
    - Isso pode gerar **ganho térmico indesejado**, elevando a temperatura interna da edificação.
    """)

        


elif pagina_selecionada == "Carga Térmica Total":
    st.subheader("Carga Térmica Total")
    st.markdown("""
            <div style="text-align: justify;">
            A carga térmica total é a quantidade de calor que deve ser removida ou adicionada a um ambiente para manter 
            as condições de conforto térmico desejadas. Essa carga é influenciada por diversos fatores, como a 
            temperatura externa, a umidade relativa do ar, a radiação solar, as características construtivas do 
            edifício e o número de ocupantes. Após os calculos realizados, a carga térmica total
            da Paróquia São Francisco de Assis está descrita na tabela abaixo:
            """, unsafe_allow_html=True)
        
        # Dados da tabela de carga térmica
    dados_carga = {
        "Fonte de Carga": [
            "Iluminação",
            "Público (ocupação)",
            "Insolação total",
            "Infiltração",
            "Ventilação",
            "Equipamentos"
        ],
        "Potência (W)": [
            391.28,
            40286.00,
            93147.53,
            46251.67,
            17651.83,
            3287.50
        ],
        "Potência (BTU/h)": [
            1335.71,
            137434.63,
            317791.04,
            157827.41,
            60261.55,
            11218.15
        ]
    }

    # Criar o DataFrame
    df_carga = pd.DataFrame(dados_carga)

    # Calcular os totais
    total_watts = df_carga["Potência (W)"].sum()
    total_btu = df_carga["Potência (BTU/h)"].sum()

    
    st.table(df_carga)

    # Exibir os totais
    st.markdown(f"**Carga Térmica Total (W): {total_watts:,.2f}**")
    st.markdown(f"**Carga Térmica Total (BTU/h): {total_btu:,.2f}**")

elif pagina_selecionada == "Sistema Proposto":
    st.subheader("Sistema Proposto")
    st.markdown("""
            <div style="text-align: justify;">
            O sistema de climatização proposto para a Paróquia
            São Francisco de Assis é um sistema de climatização central,
            com a instalação de um sistema de climatização do tipo  split,
            com capacidade de 60.000 BTU/h, que será instalado na parte superior do altar.
            Esse sistema é adequado para atender a carga térmica total da edificação,
            proporcionando conforto térmico e eficiência energética.
            """, unsafe_allow_html=True)
    st.video('Novo Ar condicionado TETO Midea Xpower Inverter.mp4')
    
    dados_custo = {
    "Item": [
        "Ar-condicionado 60.000 BTU",
        "Instalação elétrica",
        "Instalação hidráulica",
        "Mão de obra"
    ],
    "Valor Unitário (R$)": [13498.20, 1500.00, 1800.00, 1200.00],
    "Quantidade": [12, 12, 12, 12],
    "Subtotal (R$)": [161978.40, 18000.00, 21600.00, 14400.00]
            }

    # Criar o DataFrame
    df_custo = pd.DataFrame(dados_custo)

    # Calcular o total
    total_custo = df_custo["Subtotal (R$)"].sum()

    # Exibir a tabela
    st.header("Estimativa de Custo Total (Equipamentos + Instalação)")
    st.table(df_custo)

    # Exibir o total estimado
    st.markdown(f"**Total estimado: R$ {total_custo:,.2f}**")