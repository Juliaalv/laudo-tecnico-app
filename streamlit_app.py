import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime
import plotly.graph_objects as go
import numpy as np


# Configuração da Página
st.set_page_config(page_title="Relatório de Eficiência Energética - Hotel Village", layout="wide")

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
st.sidebar.title("Páginas disponíveis")

# Seção 1: Caracterização, Diagnósticos e Recomendações
with st.sidebar.expander("Seção 1"):
    if st.button("Sobre", key="pagina_inicial", use_container_width=True):
        pagina_selecionada = "Sobre"
    
    if st.button("Responsabilidade Técnica", key="responsabilidade_tecnica", use_container_width=True):
        pagina_selecionada = "Responsabilidade Técnica"
    
    if st.button("Caracterização do Imóvel", key="caracterizacao_imovel", use_container_width=True):
        pagina_selecionada = "Caracterização do Imóvel"
    
    if st.button("Vistoria", key="vistoria", use_container_width=True):
        pagina_selecionada = "Vistoria"
    
    if st.button("Caracterização de João Pessoa", key="caracterizacao_jp", use_container_width=True):
        pagina_selecionada = "Caracterização de João Pessoa"
    
    if st.button("Diagnóstico de Conforto", key="diagnostico_conforto", use_container_width=True):
        pagina_selecionada = "Diagnóstico de Conforto"
    
    if st.button("Recomendações Técnicas", key="recomendacoes_tecnicas", use_container_width=True):
        pagina_selecionada = "Recomendações Técnicas"

# Seção 2: Novas Análises
with st.sidebar.expander("Seção 2"):
    if st.button("Carta Solar", key="carta_solar", use_container_width=True):
        pagina_selecionada = "Carta Solar"
    
    if st.button("Análise de Sombreamento", key="analise_sombreamento", use_container_width=True):
        pagina_selecionada = "Análise de Sombreamento"

    if st.button("Máscara de Penetração", key="analise_penetracao", use_container_width=True):
        pagina_selecionada = "Máscara de Penetração"
    
    if st.button("Iluminação Artificial", key="analise_ilu", use_container_width=True):
        pagina_selecionada = "Iluminação Artificial"
    
    if st.button("Recomendações Técnicas", key="recomendacoes_tecnicas2", use_container_width=True):
        pagina_selecionada = "recomendacoes tecnicas 2"

    if st.button("Análise de Viabilidade de Projeto", key="Analise_viabilidade", use_container_width=True):
        pagina_selecionada = "Analise de viabilidade"




# Exibição da página selecionada
if pagina_selecionada == "Sobre":
    st.title("Relatório de Consultoria de Eficiência Energética")
    st.subheader("Hotel Village - João Pessoa, PB")

    st.write("""
    Este relatório técnico foi ofertado para o Hotel Village Premium João Pessoa,
     inscrito no CNPJ 13.878.606/0001-76, situado na Avenida Presidente Epitácio Pessoa, 
             n° 4851, Bairro Tambaú, João Pessoa, Paraíba, CEP: 58039-020.
    """)


    # Usando um card visual para simplificar o escopo
    with st.container():
        st.markdown("""
        <div style="background-color:#f0f0f5;padding:20px;border-radius:10px">
        <h4 style="color:#333;text-align:center;">Escopo da Consultoria</h4>
        <p style="text-align:justify; color:#555;">
        O relatório abrange a análise detalhada dos sistemas e práticas energéticas do imóvel, com o objetivo de identificar 
        pontos críticos e propor melhorias para aumentar a eficiência no consumo de energia. A consultoria avaliou os principais 
        sistemas que impactavam o consumo energético do hotel, como iluminação, climatização, aquecimento de água e outros equipamentos.
        O foco foi identificar oportunidades de otimização, redução de custos operacionais e minimização do impacto ambiental. 
        Durante a consultoria, os sistemas existentes foram inspecionados para avaliar seu desempenho e identificar áreas onde 
        intervenções pudessem trazer benefícios. 
        A análise também considerou a integração desses sistemas com o ambiente, levando em conta a estrutura do edifício, 
        o clima local e as práticas operacionais. As recomendações visaram melhorar a eficiência energética do Hotel Village Premium, 
        garantindo um uso mais racional e sustentável dos recursos disponíveis.
        </p>
        </div>
        """, unsafe_allow_html=True)

elif pagina_selecionada == "Caracterização do Imóvel":
    
    # Insira o caminho ou o arquivo de vídeo
    video_file = open('HOTEL3D.mp4', 'rb')

    # Use st.video para exibir o vídeo 
    st.video(video_file, format="video/mp4", start_time=0)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Estrutura do hotel")
        st.write("""
        - 9 andares;
        - Recepção 24 horas;
        - Sala para eventos;
        - Piscina adulto e infantil com hidromassagem;
        - Academia;
        - Espaço de convivência com jogos;
        - Dois restaurantes;
        - Um elevador social e um elevador de serviço;
        """)
        
    with col2:
        
        st.subheader("Especificações Técnicas")
        st.write("""
        **Área construída:** XXX m²  
        **Número de Apartamentos:** 90   
        **Número de andares:** 9  
        **Ano de Inauguração:** 2004 
        """)
        st.subheader("Descrição do Imóvel")
        st.write("""
        O empreendimento possui 90 apartamentos divididos nas 
        categorias Standard e Premium.
        Todos os quartos incluem uma Smart TV LED de 42 polegadas, 
        frigobar, ar-condicionado split, além de um banheiro 
        privativo equipado com água quente.
        """)

    
elif pagina_selecionada == "Responsabilidade Técnica":
    st.subheader("Equipe Técnica")
    st.markdown("""
            <div style="text-align: justify;">
                A consultoria de eficiência energética do Hotel Village é conduzida por uma equipe de engenheiras altamente qualificadas, 
                com vasta experiência em energias renováveis e otimização de recursos energéticos. 
                Nossas especialistas atuam em projetos 
                de sustentabilidade, automação de sistemas prediais
                e soluções inovadoras para maximizar a eficiência energética, 
                sempre focando na redução de custos operacionais e no impacto ambiental.
            """, unsafe_allow_html=True)

    # Criação de três colunas para exibir as fotos lado a lado
    col1, col2, col3 = st.columns(3)

    # Coluna 1 - Eng. Julia Alves
    with col1:
        st.image("img/ju.jpg", caption="Eng. Julia Alves", use_column_width=True)
        st.markdown("""
        <div style="background-color:#f0f0f5;padding:10px;border-radius:10px;">
        <p style="text-align:center; color:#333;">
        Engenheira com foco em energias renováveis.
        </p>
        </div>
        """, unsafe_allow_html=True)

    # Coluna 2 - Eng. Julia Ribeiro
    with col2:
        st.image("img/ju2.jpg", caption="Eng. Julia Ribeiro", use_column_width=True)
        st.markdown("""
        <div style="background-color:#f0f0f5;padding:10px;border-radius:10px;">
        <p style="text-align:center; color:#333;">
        Engenheira especialista em eficiência energética.
        </p>
        </div>
        """, unsafe_allow_html=True)

    # Coluna 3 - Eng. Andressa Kátia
    with col3:
        st.image("img/andressa.jpg", caption="Eng. Andressa Kátia", use_column_width=True)
        st.markdown("""
        <div style="background-color:#f0f0f5;padding:10px;border-radius:10px;">
        <p style="text-align:center; color:#333;">
        Análise do consumo energético do hotel.
        </p>
        </div>
        """, unsafe_allow_html=True)

elif pagina_selecionada == "Vistoria":
    vistoria_date = datetime(2024, 8, 1)  # Data da vistoria

    st.write("Data da vistoria: 1 de Agosto de 2024.", )
    
    st.subheader("Resfriamento Artificial")
    st.markdown("""
            <div style="text-align: justify;">
            A análise dos sistemas de climatização revelou que a maioria dos ar condicionados é do tipo inverter,
             o que é mais eficiente em comparação com modelos convencionais. No entanto, foi observado que a manutenção 
             preventiva dos sistemas pode estar deficiente. Isso pode impactar 
             negativamente o desempenho e a eficiência energética dos equipamentos, 
             mesmo sendo eles inverter.
            """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("img/split_eventos.jpg", use_column_width=True)
    with col2:
        st.image("img/split_quarto.jpg", use_column_width=True)
    with col3:
        st.image("img/split_recepcao.jpg", use_column_width=True)
        

    st.subheader("Iluminação")
    st.markdown("""
            <div style="text-align: justify;">
                A edificação utiliza lâmpadas LED, o que é benéfico para a eficiência energética.
                No entanto, a iluminação dos corredores não possui sensores de presença, exceto 
                nos acessos aos elevadores. A instalação de sensores de presença adicionais poderia 
                otimizar o consumo de energia, garantindo que as luzes sejam acesas apenas quando necessário. 
                Além disso, a iluminância nos apartamentos pode estar abaixo dos níveis exigidos pela
                ABNT NBR 15.575, o que pode afetar o conforto visual dos hóspedes e a funcionalidade dos ambientes.  
            """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.image("img/IMG_20240801_104201.jpg", use_column_width=True)
    with col2:
        st.image("img/IMG_20240801_104230.jpg", use_column_width=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("img/iluminacao_corredor.jpg", use_column_width=True)
    with col2:
        st.image("img/ilumi1.jpg", use_column_width=True)
    with col3:
        st.image("img/iluminacao_elevador.jpg", use_column_width=True)

    st.subheader("Aquecimento de água")    
    st.markdown("""
            <div style="text-align: justify;">
            O hotel possui coletores solares para o aquecimento de água, mas foi constatado que muitos
             deles estão em condições inadequadas, apresentando avarias como trincas, acúmulo de poeira 
             e falta de manutenção geral. Além disso, os boilers, que complementam o sistema de aquecimento, 
             também estão comprometidos, exibindo problemas como vazamentos e corrosão por ferrugem.    
            """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("img/boiler.jpg", use_column_width=True)
    with col2:
        st.image("img/coletor.jpg", use_column_width=True)
    with col3:
        st.image("img/coletores.jpg", use_column_width=True)

    

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
                Outro parâmetro importante, é o regime de nebulosidade da cidade, 
                o qual diz respeito às possíveis interferências que estas podem 
                causar ao balanço de energia radiativa (recebida/transmitida) e, 
                consequentemente, na temperatura ambiente. Considera-se o céu encoberto 
                tendo cobertura de nuvens 10 décimos. Com isso, é notável na Figura 16 
                que em todos os meses do ano ocorre nebulosidade na capital paraibana, 
                segundo as normais climatológicas do período 1991-2020. Nesse sentido, 
                percebe-se o bimestre junho-julho com a maior cobertura por nuvens, 
                ambos apresentando 7 décimos. Enquanto a média anual de nebulosidade é de 6,2 décimos.

            """, unsafe_allow_html=True)
    
    neb = go.Figure()

    neb.add_trace(go.Bar(
        x=df['Mês'],
        y=df['Nebulosidade (décimos)'],
        marker_color='purple',
        name='Nebulosidade Mensal'
    ))

    neb.update_layout(
        title='Nebulosidade Mensal (1991-2020) - João Pessoa, PB',
        xaxis_title='Mês',
        yaxis_title='Nebulosidade (décimos)',
        width=800,
        height=400
    )
    st.plotly_chart(neb)

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



elif pagina_selecionada == "Vistoria":
    st.title("Vistoria do Imóvel")
    st.write("Descrição dos resultados da vistoria realizada no hotel, identificando pontos de melhoria para eficiência energética.")
    
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

    st.image("img/carta.png", use_column_width=True)

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
    - A principal solução é o **aquecimento solar com inércia térmica**.""")
    
    st.subheader( "Conclusão")
    st.write("""
    - **Ventilação natural** é a estratégia predominante e mais eficaz em João Pessoa.
    - Para situações de calor extremo, complementação com **ar condicionado** e estratégias passivas como **inércia térmica** e **resfriamento evaporativo** é necessária.
    - **Frio** demanda mínima intervenção, com o **aquecimento solar** sendo suficiente.
    """)

elif pagina_selecionada == "Recomendações Técnicas":
    st.subheader("Ventilação Natural")

    st.markdown("""<div style="text-align: justify;">Para otimizar a ventilação natural, a integração de elementos 
        arquitetônicos como jardins verticais, que podem ser observados na 
        figura abaixo, pode ser altamente benéfica. Jardins verticais, 
        como os utilizados no Hotel Emiliano, em São Paulo, 
        não apenas melhoram a qualidade do ar, mas também 
        atuam como uma barreira contra o calor, resfriando 
        naturalmente os ambientes. Além disso, a vegetação 
        utilizada nesses jardins cria um microclima que reduz a 
        necessidade de ventilação mecânica, diminuindo o consumo energético e o impacto ambiental.""",
        unsafe_allow_html=True)

    st.image("img/jardins.png",use_column_width=True)

    st.markdown("""<div style="text-align: justify;"> Os pátios internos, observados na Figura abaixo, são outra estratégia eficaz
                que pode ser vista em hotéis como o Hotel Patio de las Cruces, em Sevilha. 
                Esses espaços permitem a ventilação cruzada, facilitando a circulação do ar fresco 
                e a saída do ar quente, promovendo uma sensação térmica mais agradável para os hóspedes. 
                Ao combinar a ventilação natural com elementos de inércia térmica e resfriamento evaporativo, 
                esses hotéis conseguem manter o conforto térmico de forma passiva e sustentável. 
                """,
        unsafe_allow_html=True)
    
    st.image("img/jardins2.png",use_column_width=True)

    st.markdown("""<div style="text-align: justify;">Dessa forma, a adoção de jardins verticais e 
                pátios internos não só melhora a eficiência da ventilação natural, 
                como também se alinha com as tendências de sustentabilidade e design bioclimático, 
                proporcionando um ambiente mais saudável e confortável para todos.
                """,
        unsafe_allow_html=True)

    st.subheader("Isolamento Térmico")

    
    st.markdown("""<div style="text-align: justify;">O uso de tapetes e carpetes espessos é uma prática 
                comum em hotéis localizados em climas quentes, como o Hotel Fasano no Rio de Janeiro 
                 e o La Mamounia em Marrakech respectivamente. Além disso, ambos os hotéis optam por 
                utilizar móveis de madeira maciça ou laminada, que possuem uma capacidade de inércia 
                térmica significativa. Esses materiais absorvem o calor do ambiente lentamente ao longo do dia e o liberam 
                de forma gradual à noite, contribuindo para uma temperatura interna mais equilibrada e confortável.
                """,
        unsafe_allow_html=True)
    
    st.image("img/fasano.png",use_column_width=True)
    st.image("img/la.png",use_column_width=True)

    st.subheader("Sistema de Resfriamento")

    st.markdown("""<div style="text-align: justify;">A manutenção adequada dos sistemas de ar condicionado
                 pode aumentar significativamente sua eficiência, reduzindo 
                o consumo de energia e prolongando a vida útil dos equipamentos.  
                Para otimizar ainda mais o desempenho dos sistemas de ar condicionado, 
                a implementação de sistemas de automação que ajustem automaticamente a 
                temperatura com base na ocupação dos quartos pode ser altamente benéfica.
                """,
        unsafe_allow_html=True)
    
    st.markdown("""<div style="text-align: justify;">Sistemas como o Connected Room, 
                utilizado pelo Hilton Hotels, não apenas proporcionam um ambiente personalizado para os hóspedes, 
                mas também contribuem para a economia de energia. O Connected Room permite que os hóspedes 
                controlem a temperatura e outros aspectos do quarto através de seus dispositivos móveis, 
                enquanto ajusta automaticamente as configurações quando o quarto está desocupado, 
                otimizando o consumo de energia e reduzindo o impacto ambiental.
                """,
        unsafe_allow_html=True)
    
    st.image("img/connected.png",use_column_width=True)
   

    st.markdown("""<div style="text-align: justify;">Ao aliar a eficiência dos sistemas de ar condicionado com a 
    automação inteligente, o hotel consegue não só melhorar a experiência 
    dos hóspedes, mas também se alinhar às tendências de sustentabilidade e 
    gestão energética, proporcionando um ambiente mais eficiente e ecologicamente responsável para todos.
                   """,
        unsafe_allow_html=True)
    
    st.subheader("Sistema de Resfriamento Passivo")

    st.markdown("""<div style="text-align: justify;">A instalação de elementos de sombreamento, como brises, 
                é uma solução eficaz para melhorar o conforto térmico em hotéis, especialmente em regiões 
                de alta incidência solar. Esses dispositivos são essenciais para reduzir a carga térmica 
                nos ambientes internos, tornando-se uma alternativa viável e sustentável em comparação 
                com o uso intensivo de sistemas de ar condicionado. Para otimizar a eficiência desses 
                elementos de sombreamento, sua integração no design arquitetônico pode ser altamente benéfica.
                   """,
        unsafe_allow_html=True)
    
    st.markdown("""<div style="text-align: justify;">Brises, como os utilizados no Oceana Atlântica Hotel, 
                em João Pessoa, são projetados para regular a entrada de luz natural nos ambientes,
                 bloqueando a radiação solar direta e permitindo a ventilação ao mesmo tempo. 
                Isso não só mantém os espaços internos mais frescos, mas também reduz a necessidade 
                de resfriamento ativo, diminuindo o consumo energético e o impacto ambiental.
                   """,
        unsafe_allow_html=True)
    
    st.image("img/hotel_brise.jpg",use_column_width=True)

    st.markdown("""<div style="text-align: justify;">Dessa forma, a adoção de brises, marquises e pergolados 
                não só melhora a eficiência energética e o conforto térmico, mas também se 
                alinha com as tendências de sustentabilidade e design bioclimático, 
                proporcionando um ambiente mais saudável e agradável para todos.
                   """,
        unsafe_allow_html=True)
    
    st.subheader("Iluminação")

    st.markdown("""<div style="text-align: justify;">A automação da iluminação é uma solução eficaz para otimizar
                 o consumo de energia em hotéis, especialmente em áreas onde a iluminação total não é sempre 
                necessária. O uso de sistemas de controle de iluminação em áreas de estar ou descanso
                 pode ajustar automaticamente a intensidade das luzes com base na presença ou ausência de pessoas. 
                Essa abordagem não só reduz o consumo de energia, mas também melhora a experiência dos hóspedes, 
                proporcionando um ambiente mais confortável e adaptado às suas necessidades.

                   """,
        unsafe_allow_html=True)

    st.markdown("""<div style="text-align: justify;">O Residencial Chapultepec One do The Ritz-Carlton, 
                na Cidade do México, utiliza o sistema de controle de iluminação Quantum da Lutron. 
                Este sistema permite um controle preciso e automatizado da iluminação, ajustando-se às 
                necessidades dos hóspedes e ao uso dos espaços, ao mesmo tempo em que otimiza o consumo de energia. 
                   """,
        unsafe_allow_html=True)
    st.image("img/lutron.png",use_column_width=True)

elif pagina_selecionada == "Carta Solar":
    st.header('Carta Solar')


    st.markdown("""
        <div style="text-align: justify;">
        A carta solar é uma ferramenta essencial no planejamento arquitetônico,
        especialmente em projetos que visam maximizar o conforto e a eficiência energética, 
        como no caso de hotéis. A conversão solar transforma a trajetória solar em uma representação
        2D para fácil leitura.

            """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
   
    with col1:
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
    
    st.markdown("""
            <div style="text-align: justify;">
            O Hotel Village Premium, voltado para o Leste, recebe mais luz solar durante as manhãs, 
            especialmente no solstício de verão. Nos equinócios, com a radiação solar incidindo sobre a
            linha do equador, João Pessoa, por estar próxima a essa linha, tem mais horas de sol do que 
            no solstício de inverno. Isso demonstra a eficácia da carta solar e destaca a vantagem da 
            localização do hotel em relação à luz natural.

            """, unsafe_allow_html=True)
    


elif pagina_selecionada == "Análise de Sombreamento":

    st.header('Análise de Sombreamento')
    st.markdown("""
            <div style="text-align: justify;">
            A análise de sombreamento de uma edificação consiste em avaliar a projeção de sombras
            ao longo do dia e do ano, considerando a localização geográfica, a orientação da construção 
             e os elementos circundantes, como outras edificações. Esse estudo permite identificar áreas de 
             edificação que estarão mais ou menos expostas à luz solar direta, auxiliando na otimização do 
             desempenho energético e no conforto dos usuários.

            """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.image("img/hotelsomb.jpg", width=400)
    with col2:
        video2 = open('tsolar2.mp4', 'rb')
        st.video(video2, format="video/mp4", start_time=0)

    st.markdown("""
            <div style="text-align: justify;">
                Para a realização da Análise de Sombreamento do Hotel Village Premium, 
                considerou-se características importantes, como altura, largura 
                e distância da vizinhança em relação ao hotel.

            """, unsafe_allow_html=True)
    data_s = {
        "Local": ["Hotel Village", "Edificação a Leste", "Edificação ao Norte", "Edificação a Oeste"],
        "Altura (m)": [23, 36, 31, 41],
        "Largura (m)": [np.nan, 42, 90, 42],
        "Distância ao Hotel (m)": [np.nan, 20, 36, 29]
    }

    df_s = pd.DataFrame(data_s)
    st.markdown(df_s.to_markdown(index=False), unsafe_allow_html=True)

    st.subheader('Vizinhança Leste')      

    st.markdown("""
            <div style="text-align: justify;">
            A máscara de sombreamento causada pela vizinhança leste no hotel afeta 
            principalmente os horários da manhã. Na Figura abaixo, a área em vermelho à 
            direita indica o período em que o sol está bloqueado pela edificação a leste,
            abrangendo as primeiras horas após o nascer do sol.
            """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.image("img/carta1.jpg", width=300)
    with col2:
         st.markdown("""
            <div style="text-align: justify;">
            <ul>
                <li><strong>Solstício de verão</strong>: Hotel sombreado até aproximadamente 9h30min; após esse horário, sol ilumina diretamente a fachada leste.</li>
                <li><strong>Equinócios</strong>: Sombreamento até cerca de 9h41min; depois, o sol começa a iluminar o hotel.</li>
                <li><strong>Solstício de inverno</strong>: Sombreamento prolongado até aproximadamente 9h48min devido à trajetória mais baixa do sol.</li>
                <li><strong>Inverno</strong>: Luz solar direta limitada nas primeiras horas da manhã devido à trajetória do sol e à presença da edificação leste.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)


    st.subheader('Vizinhança Oeste')      

    st.markdown("""
            <div style="text-align: justify;">
            Na Figura abaixo, a área vermelha à esquerda representa o sombreamento causado pela edificação à oeste. 
            
            """, unsafe_allow_html=True)
    

    col1, col2 = st.columns(2)

    with col1:
        st.image('img/sombreamento_oeste.jpg', width=300)

    with col2:
         st.markdown("""
            <div style="text-align: justify;">
            <ul>
                <li><strong>Solstício de verão</strong>: O sombreamento começa mais tarde, por volta das 14h47min, e se prolonga por um período mais curto. </li>
                <li><strong>Equinócios</strong>: O sombreamento se inicia por volta das 14h44min, à medida que o sol começa a descer no horizonte oeste.</li>
                <li><strong>Solstício de inverno</strong>: O hotel estará sombreado a partir das 15h00min, com o sombreamento se estendendo até o pôr do sol.</li>
                <li>Essa variação sazonal resulta em diferentes períodos de incidência de luz solar direta na fachada
            oeste do hotel, sendo os Equinócios os períodos mais afetados pelo sombreamento no final da tarde.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)


    
    st.subheader('Vizinhança Norte')

    st.markdown("""
            <div style="text-align: justify;">
            Na Figura a seguir, a área vermelha da máscara de sombreamento ao norte não passa 
            por nenhum solstício ou equinócio, o que significa que as obstruções ao norte 
            não impactam diretamente o hotel nos dias mais críticos em termos de trajetória solar, 
            como nos solstícios de verão e inverno, ou nos equinócios. Isso indica que a vizinhança 
            ao norte tem uma altura ou posição que não interfere nas trajetórias solares mais importantes, 
            permitindo que, durante esses períodos, o hotel receba luz solar direta sem obstruções.
            """, unsafe_allow_html=True)
    
    st.image('img/sombreamento_norte.jpg', width=300)

elif pagina_selecionada == "Máscara de Penetração":
    st.header('Máscara de Penetração')
    st.markdown("""
            <div style="text-align: justify;">
            A máscara de penetração solar é uma ferramenta usada para avaliar a incidência direta de luz solar
            em um edifício ao longo do ano. Ela mostra os períodos em que o sol penetra em diferentes ângulos 
            e alturas no ambiente interior, de acordo com a trajetória solar sazonal. Com essa análise, 
            é possível projetar elementos como brises, persianas ou varandas, 
            ajustando o sombreamento de acordo com a necessidade de iluminação e conforto térmico ao 
            longo do ano, garantindo o melhor aproveitamento da luz solar.
            Para a avaliação, usou-se as dimensões (largura, altura e peitoril) 
            das janelas da fachada leste do hotel dos quartos 304 e 305. 
            """, unsafe_allow_html=True)
    
    st.subheader('Fachada Leste')

    st.markdown("""
            <div style="text-align: justify;">
            Na Figura abaixo, a área vermelha indica a penetração solar para o apartamento 304 ao longo do ano. 
            """, unsafe_allow_html=True)
    
    
    col1, col2 = st.columns(2)

    with col1:
        st.image('img/penetracao304.jpg', width=300)

    with col2:
         st.markdown("""
            <div style="text-align: justify;">
            <ul>
                <li><strong>Solstício de inverno</strong>: Não há penetração solar no local, e a área permanece sombreada o tempo todo.</li>
                <li><strong>Equinócios</strong>: A penetração de luz solar começa às 8h55min e se estende até às 10h00min,
                totalizando 1h05min de luz direta.</li>
                <li><strong>Solstício de verão</strong>: a penetração solar inicia às 8h45min
                e se prolonga até às 9h55min, resultando em 1h10min de incidência direta.</li>
                <li>Após esses períodos, a área também permanece sombreada.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("""
            <div style="text-align: justify;">
            Na Figura abaixo, a área vermelha indica a penetração solar para o quarto 305 ao longo do ano.
            """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.image('img/penetracao305.jpg', width=300)

    with col2:
         st.markdown("""
            <div style="text-align: justify;">
            <ul>
                <li><strong>Solstício de inverno</strong>:A área recebe luz solar a partir de 
                aproximadamente 9h00min até às 10h00min, oferecendo 1h00min de insolação.</li>
                <li><strong>Equinócios</strong>:  o sol começa a incidir por volta das 8h48min e 
                segue até cerca de 10h00min, somando 1h12min de exposição solar direta.</li>
                <li><strong>Solstício de verão</strong>: O local é iluminado entre 8h30min e 9h55min, 
                após esse período de 1h25min, a área volta a ficar sombreada.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
         
elif pagina_selecionada == "Iluminação Artificial":
    st.header('Caracterização do Sistema de Iluminação Artificial')

    st.markdown("""
            <div style="text-align: justify;">
            Para a caracterização do sistema de iluminação artificial do hotel, 
            foram analisados os 90 apartamentos, divididos em duas categorias: 
            45 do tipo Standard e 45 do tipo Premium, além dos banheiros (WC) de cada unidade. 
            Cada ambiente foi equipado com lâmpadas e luminárias, variando em potência e quantidade,  
            conforme mostrado o quadro abaixo.


            """, unsafe_allow_html=True)




    dados= {
    "Tipo de Quarto": ["STANDARD (x45)", "STANDARD (x45)", "WC STANDARD (x45)", "PREMIUM (x45)", "PREMIUM (x45)", "WC PREMIUM (x45)"],
    "Equipamento": ["LÂMPADAS", "LUMINÁRIAS", "LÂMPADAS", "LÂMPADAS", "LUMINÁRIAS", "LÂMPADAS"],
    "Modelo": ["AVANT", "FOXLUX", "AVANT", "AVANT", "FOXLUX", "AVANT"],
    "Unidades": [225, 136, 45, 135, 180, 90],
    "Potência Unitária (W)": [5, 3, 5, 5, 3, 5],
    "Horas de Uso": [6075, 2028, 2025, 6075, 2025, 2025],
    "Potência Mensal (W)": [6834375, 820125, 465625, 2460375, 1822500, 911250],
    "Consumo (kWh)": [6834.375, 820.125, 465.625, 2460.375, 1822.5, 911.25]
}

    
    df_quarto = pd.DataFrame(dados)

    st.markdown(df_quarto.to_markdown(index=False), unsafe_allow_html=True)
    

    st.markdown("""
            <div style="text-align: justify;">
           O uso diário do sistema de iluminação segue um padrão: as lâmpadas dos quartos permanecem 
           ligadas por 4h30min, as luminárias por 1h30min, e as lâmpadas dos banheiros (WC) também por 1h30min, 
           tanto nos quartos Standard quanto nos Premium.
            """, unsafe_allow_html=True)


    col1, col2= st.columns(2)

    with col1:
            st.subheader('Apartamentos Standard')
            st.markdown("""
                <div style="text-align: justify;">
                <ul>
                    <li><strong>Lâmpadas:</strong> 5 lâmpadas de 5 Watts da marca Avant.</li>
                    <li><strong>Luminárias:</strong> 3 luminárias de 3 Watts, modelo FoxLux</li>
                    <li><strong>Horas de Uso Mensal (45 apt)</strong>: 6.075 horas </li>
                </ul>
                </div>
                """, unsafe_allow_html=True)

    with col2:
            st.subheader('Apartamentos Premium')
            st.markdown("""
                <div style="text-align: justify;">
                <ul>
                    <li><strong>Lâmpadas:</strong> 5 lâmpadas de 5 Watts da marca Avant.</li>
                    <li><strong>Luminárias:</strong> 3 luminárias de 3 Watts, modelo FoxLux.</li>
                    <li><strong>Horas de Uso Mensal (45 apt)</strong>: 6.075 horas.</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
    col1, col2= st.columns(2)

    with col1:
            st.subheader('Banheiros Standard')
            st.markdown("""
                <div style="text-align: justify;">
                <ul>
                    <li><strong>Lâmpadas:</strong> 1 lâmpada de 5 Watts.</li>
                    <li><strong>Horas de Uso Mensal (45 apt)</strong>: 2.025 horas. </li>
                </ul>
                </div>
                """, unsafe_allow_html=True)

    with col2:
            st.subheader('Banheiros Premium')
            st.markdown("""
                <div style="text-align: justify;">
                <ul>
                    <li><strong>Lâmpadas:</strong> 2 lâmpadas de 5 Watts.</li>
                    <li><strong>Horas de Uso Mensal (45 apt)</strong>: 2.025 horas.</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
    st.markdown("""
            <div style="text-align: justify;">
            O sistema de iluminação, que atende todos os 90 apartamentos, 
            é responsável por 24% do consumo total de energia do hotel, 
            correspondendo a 13.304,25 kWh por mês. Esse consumo, 
            ilustrado no Quadro abaixo, gera uma despesa mensal aproximada de R$ 8.142,48.
            """, unsafe_allow_html=True)
    
    col1, col2= st.columns(2)

    with col1:
            st.subheader('Modalidade Tarifária')
            st.markdown("""
                <div style="text-align: justify;">
                <ul>
                    <li><strong>Fornecimento:</strong> tarifa Verde para consumidores de alta tensão. </li>
                    <li><strong>Classificação: </strong>Classe A4 Comercial (2,3 kV a 25 kV). </li>
                    <li><strong>Ligação: </strong>Trifásica.</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)

    with col2:
            st.subheader('Tarifas Aplicadas pela ENERGISA')
            st.markdown("""
                <div style="text-align: justify;">
                <ul>
                    <li><strong>Horário de Ponta:</strong> R$ 1,9835.</li>
                    <li><strong> Horário Fora de Ponta:</strong> R$ 0,3877</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
    st.markdown("""
                <div style="text-align: justify;">
                Considerando que o consumo médio total de energia do hotel é de <strong>56.507,75 kWh mensais</strong>, 
                com um gasto total de <strong>R$ 35.402,10</strong>,Como mostra o quadro abaixo, fica evidente que o sistema de iluminação representa 
                uma parcela significativa do consumo e dos custos. Isso reforça a importância de adotar
                 medidas de otimização para aumentar a eficiência energética. 
                
                """, unsafe_allow_html=True)
    data_sistema = {
    "SISTEMA": ["TOTAL", "ILUMINAÇÃO"],
    "CONSUMO (kWh)": ['56.507,75', '13.304,25'],
    "CUSTOS (R$)": ['35.402,10', '8.142,48'] }

    df_sistema = pd.DataFrame(data_sistema)

    st.markdown(df_sistema.to_markdown(index=False), unsafe_allow_html=True)

elif pagina_selecionada == "recomendacoes tecnicas 2":

    st.header('Recomendações Técnicas')
    st.markdown("""
                <div style="text-align: justify;">
                
                Após uma análise detalhada do uso do sistema de iluminação nos 90 apartamentos, 
                a solução identificada como a mais adequada é a implementação do Philips Hue 
                Dimmer Switch – Interruptor Inteligente. Uma vantagem significativa do Philips Hue Dimmer Switch é 
                sua fácil instalação, uma vez que não requer modificações complexas na infraestrutura elétrica atual.
                 Essa solução é ideal para automatizar a iluminação de forma eficaz, permitindo a integração com 
                sistemas de iluminação inteligente, como o próprio Philips Hue. 
                
                """, unsafe_allow_html=True)
    
    st.video('dimer.mp4')

elif pagina_selecionada == "Analise de viabilidade":
    st.header('Análise de Viabilidade de Projeto')
    st.markdown("""
                <div style="text-align: justify;">
                
                Para garantir a escolha mais econômica, realizou-se uma análise de preços
                do Philips Hue Dimmer Switch em diferentes sites, visitados no dia 28 de Setembro de 2024,
                mostrados no quadro abaixo, levando em consideração a
                 disponibilidade de produtos e possíveis 
                descontos. O objetivo foi identificar a oferta mais vantajosa, a fim de sugerir a compra de 
                90 dimmers pelo canal que apresentar as melhores condições.
                """, unsafe_allow_html=True)
    data_budget = {
    "SITE": ["PHILIPS", "MERCADO LIVRE", "ALI EXPRESS"],
    "ENDEREÇO": [
        "[Link Philips](https://www.loja.lighting.philips.com/philips-hue-dimmer-switch-interruptor-inteligente-929002398606_pai/p)", 
        "[Link Mercado Livre](https://www.mercadolivre.com.br/interruptor-controle-philips-hue-wireless-dimmer-sem-fio/p/MLB27693403?item_id=MLB4135250034&from=gshop&matt_tool=14372353&matt_word=&matt_source=google&matt_campaign_id=14302215552&matt_ad_group_id=150145935327&matt_match_type=&matt_network=g&matt_device=c&matt_creative=649558500191&matt_keyword=&matt_ad_position=&matt_ad_type=pla&matt_merchant_id=735098639&matt_product_id=MLB27693403-product&matt_product_partition_id=2269030433745&matt_target_id=pla-2269030433745&cq_src=google_ads&cq_cmp=14302215552&cq_net=g&cq_plt=gp&cq_med=pla&gad_source=1&gclid=CjwKCAjw9eO3BhBNEiwAoc0-jTR-pZc_6_Y7dO2_Pw2k_hNcRqCmUZCSgVSsA9wpRfxtXdrpWoHV3hoC0EoQAvD_BwE)", 
        "[Link Ali Express](https://pt.aliexpress.com/item/1005004159043961.html?src=google&src=google&albch=shopping&acnt=768-202-3196&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005004159043961&ds_e_product_merchant_id=108380150&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=21461839805&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjw9eO3BhBNEiwAoc0-jcEZx2pyif5ikroRU75rh6t9RB6s4wX5cvTdgU-WD2RZF9W5C57RFBoCNj4QAvD_BwE)"
    ],
    "PREÇO (R$)": ['19.710,00', '16.131,60', '14.119,20']
}

    budget_table = pd.DataFrame(data_budget)

# Para exibir os links na tabela
    st.markdown(budget_table.to_markdown(index=False), unsafe_allow_html=True)
    st.subheader('Payback')
    st.markdown("""
                <div style="text-align: justify;">
                Após o alinhamento técnico realizado em 28 de setembro de 2024 com a atual
                 gerente do hotel, foi estimado que a implementação da solução proposta poderá 
                gerar uma economia de 10% a 15% no sistema de iluminação dos apartamentos. 
                Essa estimativa baseia-se na eficiência energética proporcionada pelo uso de dimmers, 
                que permitem um controle mais preciso da intensidade luminosa, e consequentemente, 
                no menor consumo de energia sem comprometer o conforto dos hóspedes. 
                Com base nessa projeção, foi realizada uma análise de payback, considerando 
                os dois cenários de economia: 10% e 15%, ilustrado no quadro abaixo. 
                
                """, unsafe_allow_html=True)
    data_scenarios = {
    "CENÁRIOS": ["10%", "15%"],
    "CONSUMO (kWh)": ['1330,43', '1995,64'],
    "ECONOMIA MENSAL (R$)": ['814,25', '1221,37']
    }


    scenarios_table = pd.DataFrame(data_scenarios)
    st.markdown(scenarios_table.to_markdown(index=False), unsafe_allow_html=True)
    
    st.markdown("""
                <div style="text-align: justify;">
                Considerando o a terceira opção de orçamento proposto,
                 o cenário em que a economia de energia atinge 10%, o período de payback 
                estimado é de 18 meses. Já no cenário em que a economia alcança 15%, 
                o tempo de retorno é reduzido para 12 meses, tornando o investimento mais atrativo 
                e eficiente em termos de economia de energia.
                
                """, unsafe_allow_html=True)