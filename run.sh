#!/bin/bash

echo "🔄 Запуск FDL-MetaCore..."
MODE=${1:-cli}

if [ "$MODE" == "streamlit" ]; then
    echo "🌐 Запуск Streamlit UI"
    streamlit run interfaces/streamlit_ui/app.py
else
    echo "🧠 Запуск CLI-агента"
    python cli_core/cli_main.py --init SigmaAgent
fi
