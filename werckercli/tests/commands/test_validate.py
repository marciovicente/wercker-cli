import mock

from werckercli.tests import TestCase
from werckercli.commands.validate import validate


class ValidationTests(TestCase):

    @mock.patch("os.path.isfile", mock.Mock(return_value=False))
    def test_warns_when_wercker_json_not_exists(self):

        with mock.patch("werckercli.cli.puts", mock.Mock()) as puts:
            validate()

            puts.assert_called_one()

    @mock.patch("os.path.isfile", mock.Mock(return_value=True))
    def test_puts_error_when_wercker_json_could_not_be_opened(self):
        e = IOError('foo')
        with mock.patch("os.open", mock.Mock(side_effect=e)) as open:
            with mock.patch("werckercli.cli.puts", mock.Mock()) as puts:
                validate()
                open.assert_called_once()
                puts.assert_called_once()