ARG BASE_CONTAINER=jupyter/scipy-notebook

FROM ${BASE_CONTAINER}

USER ${NB_UID}

# JSXGraph
COPY --chown=${NB_UID}:${NB_GID} ./ /tmp/jsxgraph-magic/

RUN cd /tmp/jsxgraph-magic && \
    pip install --quiet --no-cache-dir -e . && \
    fix-permissions "${CONDA_DIR}" && \
    rm -rf /tmp/jsxgraph-magic

WORKDIR "${HOME}"

CMD ["start-notebook.sh", "--LabApp.collaborative=True"]