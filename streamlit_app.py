import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuração da Página
st.set_page_config(page_title="Relatório de Eficiência Energética - Hotel Village", layout="wide")

# Estilo da Sidebar e Navegação
st.sidebar.title("Navegação")
st.sidebar.info("Utilize o menu abaixo para navegar pelas seções do relatório.")
secoes = ["Página Inicial", "Caracterização Geral", "Escopo", "Descrição do Imóvel", 
          "Responsabilidade Técnica", "Vistoria", "Carta Bioclimática", "Diagnóstico de Conforto", 
          "Soluções para Eficiência Energética", "Conclusão"]

pagina = st.sidebar.radio("Ir para:", secoes)

# Página Inicial
if pagina == "Página Inicial":
    st.title("Relatório de Consultoria de Eficiência Energética")
    st.subheader("Hotel Village - João Pessoa, PB")
    st.write("""
    Este relatório apresenta os resultados da consultoria de eficiência energética realizada no Hotel Village, 
    localizado em João Pessoa, PB. O objetivo é identificar oportunidades de melhoria no consumo energético do hotel 
    e propor soluções para otimizar a eficiência energética.
    """)
    #st.image("caminho/para/imagem_do_hotel.jpg", caption="Hotel Village", use_column_width=True)

# Caracterização Geral do Objeto
elif pagina == "Caracterização Geral":
    st.header("Caracterização Geral do Objeto")
    st.subheader("Localização")
    m = folium.Map(location=[-7.11532, -34.861], zoom_start=15)
    folium.Marker([-7.11532, -34.861], tooltip="Hotel Village").add_to(m)
    st_folium(m, width=700, height=500)

    st.subheader("Endereço")
    st.write("Av. Epitácio Pessoa, 4851 - Tambaú, João Pessoa - PB, 58039-000, Brasil")
    st.write("""
    O Hotel Village está estrategicamente localizado no bairro Tambaú, uma área conhecida por sua proximidade com as 
    principais atrações turísticas de João Pessoa, além de fácil acesso a serviços e comércio.
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

# Descrição do Imóvel
elif pagina == "Descrição do Imóvel":
    st.header("Descrição do Imóvel")
    st.subheader("Características Gerais")
    st.write("""
    O Hotel Village é um edifício de 4.851 metros quadrados, com 84 quartos distribuídos em 4 andares. 
    O hotel foi construído em 1992 e passou por reformas recentes para modernização das instalações elétricas e de 
    iluminação.
    """)

    st.subheader("Especificações Técnicas")
    st.write("""
    **Área construída:** 4.851 m²  
    **Número de quartos:** 84  
    **Número de andares:** 4  
    **Ano de construção:** 1992  
    **Materiais predominantes:** Concreto, vidro, alumínio
    """)

    #st.image("caminho/para/imagem_do_imovel.jpg", caption="Fachada do Hotel", use_column_width=True)

# Responsabilidade Técnica
elif pagina == "Responsabilidade Técnica":
    st.header("Responsabilidade Técnica")
    st.write("""
    A equipe responsável pela consultoria de eficiência energética do Hotel Village é composta por profissionais com 
    vasta experiência na área de energias renováveis e eficiência energética.
    """)

    st.subheader("Equipe Técnica")
    st.write("""
    **Eng. Julia Alves** - Engenheira de Energias Renováveis  
    Especialista em análise de consumo energético e otimização de sistemas elétricos.
    
    **Eng. Julia Ribeiro** - Especialista em Eficiência Energética  
    Foco em soluções para edificações comerciais e residenciais.
    
    **Eng. Andressa Silva** - Analista de Projetos  
    Responsável pela coordenação técnica e implementação das soluções propostas.
    """)

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
    #st.image("caminho/para/carta_bioclimatica.png", caption="Carta Bioclimática", use_column_width=True)

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