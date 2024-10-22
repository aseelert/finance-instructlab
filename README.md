# finance-instructlab
 qna - for skill and knowledge


```bash
sudo dnf install gcc gcc-c++ make git python3.11 python3.11-devel
```
```bash
mkdir ~/instructlab-finance
cd ~/instructlab-finance
```

```bash
python3.11 -m venv --upgrade-deps venv-finance
source ~/instructlab-finance/venv-finance/bin/activate
pip install pip --upgrade
pip install instructlab
pip install vllm
```

```bash
ilab config init
```


```bash
(venv-finance) aseelert:instructlab-finance$ ilab config init
Welcome to InstructLab CLI. This guide will help you to setup your environment.
Please provide the following values to initiate the environment [press Enter for defaults]:
Path to taxonomy repo [/home/aseelert/.local/share/instructlab/taxonomy]:
`/home/aseelert/.local/share/instructlab/taxonomy` seems to not exist or is empty. Should I clone https://github.com/instructlab/taxonomy.git for you? [Y/n]: y
Path to your model [/home/aseelert/.cache/instructlab/models/merlinite-7b-lab-Q4_K_M.gguf]:

Generating `/home/aseelert/.config/instructlab/config.yaml`...
Please choose a train profile to use.
Train profiles assist with the complexity of configuring InstructLab training for specific GPU hardware.
You can still take advantage of hardware acceleration for training even if your hardware is not listed.
[0] No profile (CPU, Apple Metal, AMD ROCm)
[1] Nvidia A100/H100 x2 (A100_H100_x2.yaml)
[2] Nvidia A100/H100 x4 (A100_H100_x4.yaml)
[3] Nvidia A100/H100 x8 (A100_H100_x8.yaml)
[4] Nvidia L40 x4 (L40_x4.yaml)
[5] Nvidia L40 x8 (L40_x8.yaml)
[6] Nvidia L4 x8 (L4_x8.yaml)
Enter the number of your choice [hit enter for hardware defaults] [0]: 0
No profile selected - any hardware acceleration for training must be configured manually.
Initialization completed successfully, you're ready to start using `ilab`. Enjoy!
```

```bash
ilab model download
ilab model download --repository=instructlab/granite-7b-lab ###ensure HF_TOKEN is set with API key
ilab model list
```

```bash
cd ~/instructlab-finance
git clone https://github.com/aseelert/finance-instructlab.git
```
```bash
mkdir -p ~/.local/share/instructlab/taxonomy/compositional_skills/grounded/finance/table-analytics
mkdir -p ~/.local/share/instructlab/taxonomy/knowledge/finance/general
```
```bash
cp finance-instructlab/taxonomy/knowledge/finance/general/qna.yaml \
~/.local/share/instructlab/taxonomy/compositional_skills/grounded/finance/table-analytics/qna.yaml

cp finance-instructlab/taxonomy/knowledge/finance/general/qna.yaml \
~/.local/share/instructlab/taxonomy/knowledge/finance/general/qna.yaml
```

```bash
ilab taxonomy diff

knowledge/finance/general/qna.yaml
compositional_skills/grounded/finance/table-analytics/qna.yaml
Taxonomy in /home/aseelert/.local/share/instructlab/taxonomy is valid :)
```

#### Start watsonx-openai-api proxy
```bash
docker run -d -p 8080:8000 --name watsonxai-endpoint \
-e WATSONX_IAM_APIKEY=${WATSONX_IAM_APIKEY} \
-e WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID} \
-e WATSONX_REGION=${WATSONX_REGION} \
aseelert/watsonxai-endpoint:1.0
```

#### Start synthetic data generation with watsonx.ai
```bash
ilab data generate \
 --pipeline full \
 --sdg-scale-factor 10 \
 --endpoint-url http://localhost:8080/v1 \
 --output-dir ./ibm-granite-finance \
 --batch-size 8 \
 --chunk-word-count 1000 \
 --num-cpus 8 \
 --model ibm/granite-20b-multilingual
 ```

#### Instructlab Cleanup
```bash
# Remove all files in the specified InstructLab directories
rm -rf ~/.cache/instructlab/models
rm -rf ~/.local/share/instructlab
rm -rf ~/.config/instructlab
```

