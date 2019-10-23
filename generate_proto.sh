#!/usr/bin/env bash
PROTO_IMPORT_DIR="./proto"
GEN_OUT_DIR="./python/__generated__"

# Create the generated output dir if it doesn't exist
if [ ! -d "$GEN_OUT_DIR" ]; then
  mkdir -p ${GEN_OUT_DIR}
fi

# Generate python codes
protoc \
    -I=${PROTO_IMPORT_DIR} \
    --python_out=${GEN_OUT_DIR} \
    --mypy_out=${GEN_OUT_DIR} \
    ${PROTO_IMPORT_DIR}/book.proto

