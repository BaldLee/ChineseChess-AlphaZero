source activate
git clone https://github.com.cnpmjs.org/BaldLee/ChineseChess-AlphaZero.git
conda create -n chess --clone tensorflow_py3
conda activate chess
cd ChineseChess-AlphaZero
pip install -r requirements.txt
