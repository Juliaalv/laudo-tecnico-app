import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# Configuração da Página
st.set_page_config(page_title="Relatório de Eficiência Energética - Hotel Village", layout="wide")

# Estilo da Sidebar e Navegação
st.sidebar.title("Navegação")
st.sidebar.info("Utilize o menu abaixo para navegar pelas seções do relatório.")
secoes = ["Pagina Inicial","Caracterização do Imóvel", "Responsabilidade Técnica", "Vistoria",
          "Diagnóstico de Conforto", "Soluções para Eficiência Energética", "Conclusão"]

pagina = st.sidebar.radio("Ir para:", secoes)

if pagina == "Pagina Inicial":
    st.title("Relatório de Consultoria de Eficiência Energética")
    st.subheader("Hotel Village - João Pessoa, PB")

    st.write("""
    Este relatório técnico foi solicitado pelo Hotel Village Premium João Pessoa,
    inscrito no CNPJ XX.XXX.XXX/XXXX-XX, situado na Avenida Presidente Epitácio Pessoa, n° 4851, 
    Bairro Tambaú, João Pessoa, Paraíba, CEP: 58039-020.
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
    m = folium.Map(location=[-7.118022201858272, -34.82780018465539], zoom_start=15)
    folium.Marker([-7.118022201858272, -34.82780018465539], tooltip="Hotel Village").add_to(m)
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
        **Ano de construção:** 1992  
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
    st.write("""
                A consultoria de eficiência energética do Hotel Village é conduzida por uma equipe de engenheiras altamente qualificadas, 
                com vasta experiência em energias renováveis e otimização de recursos energéticos. 
                Nossas especialistas atuam em projetos 
                de sustentabilidade, automação de sistemas prediais
                e soluções inovadoras para maximizar a eficiência energética, 
                sempre focando na redução de custos operacionais e no impacto ambiental
    """)

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
        Engenheira especializada em conforto ambiental.
        </p>
        </div>
        """, unsafe_allow_html=True)
    
# Vistoria
elif pagina == "Vistoria":
    vistoria_date = datetime(2024, 8, 1)  # Data da vistoria

    st.write("Data da vistoria: 1 de Agosto de 2024.", )
    
    st.subheader("Aquecimento de água")    
    st.write("""
             
             O hotel possui coletores solares para o aquecimento de água, mas foi constatado que muitos
             deles estão em condições inadequadas, apresentando avarias como trincas, acúmulo de poeira 
             e falta de manutenção geral. Além disso, os boilers, que complementam o sistema de aquecimento, 
             também estão comprometidos, exibindo problemas como vazamentos e corrosão por ferrugem.
             
             """)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("img\\boilers.jpg", use_column_width=True)
    with col2:
        st.image("img\\coletor.jpg", use_column_width=True)
    with col3:
        st.image("img\\coletores.jpg", use_column_width=True)
    
    
    st.subheader("Climatização")
    st.write("""
             A análise dos sistemas de climatização revelou que a maioria dos ar condicionados é do tipo inverter,
             o que é mais eficiente em comparação com modelos convencionais. No entanto, foi observado que a manutenção 
             preventiva dos sistemas pode estar deficiente. Isso pode impactar 
             negativamente o desempenho e a eficiência energética dos equipamentos, 
             mesmo sendo eles inverter.""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("img\split_eventos.jpg", use_column_width=True)
    with col2:
        st.image("img\split_quarto.jpg", use_column_width=True)
    with col3:
        st.image("img\split_recepcao.jpg", use_column_width=True)
        
        
    st.subheader("Iluminação")
    st.write("""
                A edificação utiliza lâmpadas LED, o que é benéfico para a eficiência energética.
                No entanto, a iluminação dos corredores não possui sensores de presença, exceto 
                nos acessos aos elevadores. A instalação de sensores de presença adicionais poderia 
                otimizar o consumo de energia, garantindo que as luzes sejam acesas apenas quando necessário. 
                Além disso, a iluminância nos apartamentos pode estar abaixo dos níveis exigidos pela
                ABNT NBR 15.575, o que pode afetar o conforto visual dos hóspedes e a funcionalidade dos ambientes. """)



# Carta Bioclimática
elif pagina == "Diagnóstico de Conforto":

    st.subheader("Zonas Bioclimáticas")
    st.write("""
                As zonas bioclimáticas são regiões geográficas classificadas de acordo com as características 
                climáticas predominantes, como temperatura, umidade, radiação solar e velocidade do vento. 
                Essa classificação permite a análise do comportamento climático de uma área específica, 
                auxiliando no desenvolvimento de estratégias de construção e design que otimizam o conforto térmico, 
                a eficiência energética e a sustentabilidade de edificações.

    """)
    st.write("""
             Para o presente relatório, utilizamos a análise das zonas bioclimáticas para identificar
             as estratégias mais adequadas às condições climáticas da região de João Pessoa. 
             Isso permite uma abordagem personalizada e assertiva, garantindo que as recomendações 
             apresentadas sejam realmente eficazes e possam contribuir para a redução dos custos operacionais 
            e o aumento da sustentabilidade do hotel.

            Dessa forma, elas foram determinadas a partir do software Analysis-BIO, 
            o qual oferece dois métodos principais para definir as zonas bioclimáticas: 
            o TRY (Test Reference Year) e as Retas Normais. O método TRY é mais preciso, 
            pois trabalha com uma nuvem de dados composta por informações diárias de temperatura, 
            umidade e outros parâmetros climáticos ao longo do ano. No entanto, o banco de dados 
            do software não possui a cidade de João Pessoa no método TRY.

            Diante dessa limitação, utilizamos o método das retas normais para traçar as zonas bioclimáticas
            de João Pessoa. Esse método utiliza as temperaturas médias, mínimas e máximas de cada mês para definir 
            o comportamento climático da região. Embora menos detalhado que o TRY, as retas normais ainda fornecem 
            uma base sólida para a análise das condições climáticas e para a formulação de estratégias de eficiência 
            energética e conforto térmico específicas para a região. Logo, as Retas Normais delimitadas para a cidade 
            João Pessoa na carta bioclimática estão expostas na Figura abaixo.
             
             """)
    
    html_table = """
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
            <td style="border: 1px solid black;" colspan="3"><strong>Total de Desconforto:</strong> 72,47</td>
        </tr>
        <tr>
            <td style="border: 1px solid black;" colspan="3"><strong>Conforto:</strong> 27,53</strong></td>
        </tr>
    </table>
    """

    # Exibir a tabela HTML no Streamlit
    st.write("Diagnóstico de Conforto e Desconforto Térmico")
    st.markdown(html_table, unsafe_allow_html=True)


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
