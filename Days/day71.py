"""Visualizações interativas de dados"""

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool

# Dados
dados = {"x": [1, 2, 3, 4, 5], "y": [5, 6, 2, 4, 7], "nome": ["A", "B", "C", "D", "E"]}
source = ColumnDataSource(dados)

# Cria o gráfico
p = figure(
    title="Gráfico de Dispersão Interativo com Tooltips",
    x_axis_label="Eixo X",
    y_axis_label="Eixo Y",
    tools="pan,wheel_zoom,box_zoom,reset,save,hover",
    width=600,
    height=400,
    output_backend="webgl",
)

# Adiciona os pontos
p.scatter(
    "x", "y", size=15, source=source, color="navy", alpha=0.6, selection_color="red"
)

# Configura o tooltip
hover = p.select_one(HoverTool)
hover.tooltips = [
    ("Nome", "@nome"),
    ("X", "@x"),
    ("Y", "@y"),
]

show(p)
