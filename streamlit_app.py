import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(page_title="Relatório de Eficiência Energética - Hotel Village", layout="wide")

# Estilo da Sidebar e Navegação
st.sidebar.title("Navegação")
st.sidebar.info("Utilize o menu abaixo para navegar pelas seções do relatório.")
secoes = ["Pagina Inicial","Caracterização do Imóvel", "Responsabilidade Técnica", "Vistoria", "Caracterização João Pessoa",
          "Diagnóstico de Conforto", "Recomendações Técnicas"]

pagina = st.sidebar.radio("Ir para:", secoes)

if pagina == "Pagina Inicial":
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
    
    
    
    #st.image("img\logo.png", caption="Hotel Village", use_column_width=True, width=20)

# Página Inicial
elif pagina == "Caracterização do Imóvel":
    
    st.subheader("Localização do Hotel")
    m = folium.Map(location=[-7.119012285515138, -34.82788601966975], zoom_start=15)
    folium.Marker([-7.119012285515138, -34.82788601966975], tooltip="Hotel Village").add_to(m)
    st_folium(m, width=1200, height=400) 

   
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



# Responsabilidade Técnica
elif pagina == "Responsabilidade Técnica":

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
        Análise do consumo energético do hotel, identificação de possíveis ineficiências e pontos críticos.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
# Vistoria
elif pagina == "Vistoria":
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
        st.image("img\split_eventos.jpg", use_column_width=True)
    with col2:
        st.image("img\split_quarto.jpg", use_column_width=True)
    with col3:
        st.image("img\split_recepcao.jpg", use_column_width=True)
        

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
        st.image("img\IMG_20240801_104201.jpg", use_column_width=True)
    with col2:
        st.image("img\IMG_20240801_104230.jpg", use_column_width=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("img\iluminacao_corredor.jpg", use_column_width=True)
    with col2:
        st.image("img\ilumi1.jpg", use_column_width=True)
    with col3:
        st.image("img\iluminacao_elevador.jpg", use_column_width=True)

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

elif pagina == "Caracterização João Pessoa":  
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

    # Criando o gráfico com Plotly Graph Objects
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


# Carta Bioclimática
elif pagina == "Diagnóstico de Conforto":

    st.subheader("Zonas Bioclimáticas")
 
    st.markdown("""<div style="text-align: justify;">As zonas bioclimáticas são regiões geográficas classificadas de acordo com as características 
                climáticas predominantes, como temperatura, umidade, radiação solar e velocidade do vento. 
                Essa classificação permite a análise do comportamento climático de uma área específica, 
                auxiliando no desenvolvimento de estratégias de construção e design que otimizam o conforto térmico, 
                a eficiência energética e a sustentabilidade de edificações.
                Utilizamos o método das retas normais para traçar as zonas bioclimáticas
                de João Pessoa. Logo, as Retas Normais delimitadas para a cidade 
                João Pessoa na carta bioclimática estão expostas na figura abaixo.""", unsafe_allow_html=True)

    st.image("img\carta.png", use_column_width=True)

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


# Soluções para Eficiência Energética
elif pagina == "Recomendações Técnicas":
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

    st.image("img\jardins.png",use_column_width=True)

    st.markdown("""<div style="text-align: justify;"> Os pátios internos, observados na Figura abaixo, são outra estratégia eficaz
                que pode ser vista em hotéis como o Hotel Patio de las Cruces, em Sevilha. 
                Esses espaços permitem a ventilação cruzada, facilitando a circulação do ar fresco 
                e a saída do ar quente, promovendo uma sensação térmica mais agradável para os hóspedes. 
                Ao combinar a ventilação natural com elementos de inércia térmica e resfriamento evaporativo, 
                esses hotéis conseguem manter o conforto térmico de forma passiva e sustentável. 
                """,
        unsafe_allow_html=True)
    
    st.image("img\jardins2.png",use_column_width=True)

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
    
    st.image("img\connected.png",use_column_width=True)
   

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
    
    st.image("img\hotel_brise.jpg",use_column_width=True)

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
    st.image("img\lutron.png",use_column_width=True)

with st.sidebar:
    st.info("Para mais informações, acesse o relatório completo:")
    st.image("img/qrcode_relatório.png", width=200)