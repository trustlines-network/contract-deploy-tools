from setuptools import setup, find_packages

setup(
    name="contract-deploy-tools",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "py-solc",
        "web3>=5.0.0,<5.2",
        "eth-tester[py-evm]",
        "eth-utils",
        "eth-keyfile",
        "click",
    ],
    entry_points="""
    [console_scripts]
    deploy-tools=deploy_tools.cli:main
    [pytest11]
    deploy-tools=deploy_tools.plugin
    """,
)
