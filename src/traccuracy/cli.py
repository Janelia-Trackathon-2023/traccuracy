import typer

app = typer.Typer()


@app.command()
def run_ctc():
    pass


@app.command()
def run_aogm():
    pass


@app.command()
def run_divisions():
    pass


if __name__ == "__main__":
    app()
