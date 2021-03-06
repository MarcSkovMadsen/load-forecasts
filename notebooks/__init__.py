echart = {
    "title": {"text": "Graph 简单示例"},
    "tooltip": {},
    "animationDurationUpdate": 1500,
    "animationEasingUpdate": "quinticInOut",
    "series": [
        {
            "type": "graph",
            "layout": "none",
            "symbolSize": 50,
            "roam": True,
            "label": {"show": True},
            "edgeSymbol": ["circle", "arrow"],
            "edgeSymbolSize": [4, 10],
            "edgeLabel": {"fontSize": 20},
            "data": [
                {"name": "AAAA", "x": 300, "y": 300},
                {"name": "BBBB", "x": 800, "y": 300},
                {"name": "CCCC", "x": 550, "y": 100},
                {"name": "DDDD", "x": 550, "y": 500},
            ],
            "links": [
                {
                    "source": 0,
                    "target": 1,
                    "symbolSize": [5, 20],
                    "label": {"show": True},
                    "lineStyle": {"width": 5, "curveness": 0.2},
                },
                {
                    "source": "BBBB",
                    "target": "AAAA",
                    "label": {"show": True},
                    "lineStyle": {"curveness": 0.2},
                },
                {"source": "AAAA", "target": "CCCC"},
                {"source": "BBBB", "target": "CCCC"},
                {"source": "BBBB", "target": "DDDD"},
                {"source": "AAAA", "target": "DDDD"},
            ],
            "lineStyle": {"opacity": 0.9, "width": 2, "curveness": 0},
        }
    ],
}
