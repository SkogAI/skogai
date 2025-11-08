#!/usr/bin/bash

source $SKOGAI/dev/smol/.venv/bin/activate
if [ -t 0 ]; then
  skogsmol --model-type=LiteLLMModel --api-key="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" --api-base=https://openrouter.ai/api/v1 --model-id=openrouter/google/gemini-2.5-flash-preview-05-20 "$@"
else

  # /home/skogix/skogai-git/smol/.venv/bin/smolagent --model-type=LiteLLMModel --api-key=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 --api-base=https://openrouter.ai/api/v1 --model-id=openrouter/google/gemini-2.5-flash-preview-05-20 "$@"
  skogsmol --model-type=LiteLLMModel --api-key="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" --api-base=https://openrouter.ai/api/v1 --model-id=openrouter/google/gemini-2.5-flash-preview-05-20 "$@" <&0

fi
# uvx --from smolagents smolagent --model-type=LiteLLMModel --api-key=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 --api-base=https://openrouter.ai/api/v1 --model-id=openrouter/google/gemini-2.5-flash-preview-05-20 "$@"
