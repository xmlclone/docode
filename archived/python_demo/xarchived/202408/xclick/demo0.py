import click
import logging

from pathlib import Path
from typing import Union, IO


logger = logging.getLogger(__name__)


@click.group()
def main():
    ...


@click.command()
@click.option('-e', '--epoch', type=int, default=10, show_default=True, help="训练预期次数")
@click.option('-m', '--initmodel', is_flag=True, help="指定此参数后，表示不从本地加载已训练模型，而是加载最初始的BERT模型")
@click.option('-t', '--trainfile', type=click.Path(exists=True, file_okay=True, dir_okay=False), required=True, help="训练文件路径")
@click.option('-p', '--testfile', type=click.Path(exists=True, file_okay=True, dir_okay=False), help="训练完成后测试文件路径(默认为 trainfile 指定的文件)")
def train(epoch: int, initmodel: bool, trainfile: Path, testfile: Union[Path, None]):
    logger.debug(f"{epoch=}, {initmodel=}, {trainfile=}, {testfile=}")


@click.command()
@click.option('-p', '--path', type=click.Path(file_okay=True, dir_okay=True, exists=True), default=10, show_default=True, help="需要预测的RF结果路径(会解析所有xml文件)")
def predict(path: Union[Path, IO]):
    logger.debug(f"{path=}")


main.add_command(train)
main.add_command(predict)


if __name__ == '__main__':
    main()