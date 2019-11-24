#!/usr/bin/env bash
# PROTO_IMPORT_DIR="./proto"
# PROTO_FILES="./proto/**/*.proto"
# GEN_OUT_DIR="./__generated__"
PROTO_IMPORT_DIR="./"
PROTO_FILES="./proto/**/*.proto"
GEN_OUT_DIR="./"

# # Clean up the generated output dir
# if [ -d "$GEN_OUT_DIR" ]; then
#   rm -r ${GEN_OUT_DIR}
# fi

# # Create the generated output dir if it doesn't exist
# if [ ! -d "$GEN_OUT_DIR" ]; then
#   mkdir -p ${GEN_OUT_DIR}
# fi

# Generate python codes
protoc \
    -I=${PROTO_IMPORT_DIR} \
    --python_out=${GEN_OUT_DIR} \
    --mypy_out=${GEN_OUT_DIR} \
    ${PROTO_FILES}
