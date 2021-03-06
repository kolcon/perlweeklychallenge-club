use strict;
use warnings;
use feature 'say';
sub is_anagram {
    my ($word1, $word2) = @_;
    return 0 if length $word1 != length $word2;
    my $letters1 = join "", sort split "", $word1;
    my $letters2 = join "", sort split "", $word2;
    return $letters1 eq $letters2
}
my $word = "post";
for (qw /past post spot tops taps pots top/) {
    say "$word $_\t", is_anagram($word, $_) ? "True" : "False";
}
