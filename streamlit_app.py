import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuração da Página
st.set_page_config(page_title="Relatório de Eficiência Energética - Hotel Village", layout="wide")

# Estilo da Sidebar e Navegação
st.sidebar.title("Navegação")
st.sidebar.info("Utilize o menu abaixo para navegar pelas seções do relatório.")
secoes = ["Página Inicial", "Caracterização Geral", "Escopo", 
          "Responsabilidade Técnica", "Vistoria", "Carta Bioclimática", "Diagnóstico de Conforto", 
          "Soluções para Eficiência Energética", "Conclusão"]

pagina = st.sidebar.radio("Ir para:", secoes)

# Página Inicial
if pagina == "Página Inicial":
    st.title("Relatório de Consultoria de Eficiência Energética")
    st.subheader("Hotel Village - João Pessoa, PB")
    st.write("""
    Este relatório técnico foi solicitado pelo Hotel Village Premium João Pessoa,
    inscrito no CNPJ XX.XXX.XXX/XXXX-XX, situado na Avenida Presidente Epitácio Pessoa, n° 4851, 
    Bairro Tambaú, João Pessoa, Paraíba, CEP: 58039-020. O objetivo deste relatório é identificar 
    os principais pontos críticos relacionados ao consumo de energia, sistemas de aquecimento, iluminação,
    ventilação natural e climatização do hotel,bem como propor soluções físicas que promovam a
    eficiência energética na edificação.
    """)
    st.image("img\HOTEL.jpg", caption="Hotel Village", use_column_width=True)

# Caracterização Geral do Objeto
elif pagina == "Caracterização Geral":
    st.header("Caracterização Geral")
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Especificações Técnicas")
        st.write("""
        **Área construída:** XXX m²  
        **Número de Apartamentos:** 90  
        **Número de andares:** 9  
        **Ano de construção:** 1992  
        
        """)
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
        st.subheader("Localização do Hotel")
        m = folium.Map(location=[-7.118022201858272, -34.82780018465539], zoom_start=15)
        folium.Marker([-7.118022201858272, -34.82780018465539], tooltip="Hotel Village").add_to(m)
        st_folium(m, width=600, height=300)
   
    
    st.subheader("Descrição do Imóvel")
    st.write("""
                    O empreendimento possui 90 apartamentos divididos nas categorias Standard e Premium.
                    Todos os quartos incluem uma Smart TV LED de 42 polegadas, 
                    frigobar, ar-condicionado split, além de um banheiro privativo equipado com água quente.
                    """)


# Escopo
elif pagina == "Escopo":
    st.header("Escopo")
    st.subheader("Objetivo do Laudo")
    st.write("""
    O escopo deste laudo inclui a análise das condições atuais do hotel em relação ao consumo energético, 
    identificação de problemas e a proposição de soluções focadas em eficiência energética.
    """)
    st.subheader("Abrangência")
    st.write("""
    A análise cobre os seguintes aspectos:
    - Instalações elétricas;
    - Iluminação;
    - Sistemas de aquecimento e resfriamento;
    - Equipamentos de cozinha e lavanderia;
    - Áreas comuns e quartos.
    """)

# Responsabilidade Técnica
elif pagina == "Responsabilidade Técnica":
    st.header("Responsabilidade Técnica")
    st.write("""
    A equipe responsável pela consultoria de eficiência energética do Hotel Village é composta por profissionais com 
    vasta experiência na área de energias renováveis e eficiência energética.
    """)

    st.subheader("Equipe Técnica")

    # Criação de três colunas para exibir as fotos lado a lado
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("img\ju.jpg", caption="Eng. Julia Alves", use_column_width=True)
    with col2:
        st.image("img\ju2.jpg", caption="Eng. Julia Ribeiro", use_column_width=True)
        

    with col3:
        st.image("img\\andressa.jpg", caption="Andressa Kátia", use_column_width=True)
    
# Vistoria
elif pagina == "Vistoria":
    st.header("Vistoria")
    st.subheader("Problemas Identificados")
    st.write("""
    Durante a vistoria foram identificados os seguintes problemas relacionados à eficiência energética do Hotel Village:
    """)
    st.write("""
    - **Iluminação ineficiente em áreas comuns**  
      As lâmpadas instaladas possuem alta potência e baixo rendimento.
    - **Equipamentos de ar-condicionado antigos**  
      Unidades de ar-condicionado com baixo desempenho e consumo elevado.
    - **Falta de sistemas de monitoramento de consumo energético**  
      Ausência de dispositivos para acompanhamento em tempo real do consumo de energia.
    """)

# Carta Bioclimática
elif pagina == "Carta Bioclimática":
    st.header("Carta Bioclimática")
    st.write("A carta bioclimática do Hotel Village foi analisada para determinar o conforto térmico ao longo do ano.")
    # st.image("caminho/para/carta_bioclimatica.png", caption="Carta Bioclimática", use_column_width=True)

# Diagnóstico de Conforto
elif pagina == "Diagnóstico de Conforto":
    st.header("Diagnóstico de Conforto")
    st.subheader("Análise Climática")
    st.write("""
    Com base na carta bioclimática e em medições locais, foi identificado que o conforto térmico no hotel varia ao longo do ano.
    """)
    df = pd.DataFrame({
        "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
        "Temperatura Média (°C)": [30, 29, 28, 27, 26, 25, 24, 25, 26, 27, 28, 29],
        "Umidade Relativa (%)": [70, 72, 75, 78, 80, 83, 85, 82, 79, 75, 72, 70]
    })
    st.line_chart(df.set_index("Mês"))

# Soluções para Eficiência Energética
elif pagina == "Soluções para Eficiência Energética":
    st.header("Soluções para Eficiência Energética")
    st.write("""
    Com base na vistoria e nos problemas identificados, foram propostas as seguintes soluções para melhorar a eficiência energética do Hotel Village:
    """)
    st.subheader("Exemplo 1: Instalação de painéis solares")
    st.write("""
    Instalação de sistemas fotovoltaicos para suprir parte da demanda energética do hotel, reduzindo os custos com eletricidade.
    """)

    st.subheader("Exemplo 2: Troca de lâmpadas fluorescentes por LED")
    st.write("""
    Substituição das lâmpadas atuais por tecnologia LED, que proporciona maior durabilidade e economia de energia.
    """)

    st.subheader("Exemplo 3: Implementação de sistema de controle automatizado de iluminação")
    st.write("""
    Uso de sensores de presença e temporizadores para otimizar o uso da iluminação, reduzindo o consumo desnecessário de energia.
    """)

# Conclusão
elif pagina == "Conclusão":
    st.header("Conclusão")
    st.write("""
    A implementação das soluções propostas neste relatório contribuirá significativamente para a redução do consumo energético do Hotel Village, 
    resultando em economia de custos e melhoria na sustentabilidade ambiental do empreendimento.
    """)

st.sidebar.write("Para mais informações, entre em contato com a equipe responsável pela consultoria.")
